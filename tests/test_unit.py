import os
import sys
import time
import json
import numbers
import operator
import platform
from test.pystone import main as my_expensive_code

from nose.tools import with_setup

from pybenchmark import profile, stats, kpystones, CpuInfo, MemInfo, GProfiler
from pybenchmark.gprofiler import Node


POSITIVE_BENCHMARK_TIME = 0.1  # sec


def setup_positive_fixture():
    # callable that will be decorated and measured below
    some_code = lambda: time.sleep(POSITIVE_BENCHMARK_TIME)
    decorated = profile('test')(some_code)  # a la-carte decoration
    return_value = decorated()  # actual run/call of decorated callable


def setup_negative_fixture():
    # callable that will be decorated and measured below
    some_code = lambda: None
    decorated = profile('test_neg')(some_code)  # a la-carte decoration
    return_value = decorated()  # actual run/call of decorated callable


def setup_memory_fixture():
    # callable that will be decorated and measured below
    some_code = lambda: [[]] * 100000
    decorated = profile('test_neg')(some_code)  # a la-carte decoration
    return_value = decorated()  # actual run/call of decorated callable


@with_setup(setup_positive_fixture)
def test_dict_keys():
    assert 'test' in stats
    assert isinstance(stats['test'], dict)
    assert 'time' in stats['test']
    assert 'kstones' in stats['test']
    assert 'memory' in stats['test']


@with_setup(setup_positive_fixture)
def test_dict_values():
    assert isinstance(stats['test']['time'], float)
    assert isinstance(stats['test']['kstones'], float)
    assert isinstance(stats['test']['memory'], numbers.Real)
    assert stats['test']['time'] > 0
    assert abs((kpystones * POSITIVE_BENCHMARK_TIME) - stats['test']['kstones']) < (kpystones / 10)
    assert stats['test']['memory'] >= 0


@with_setup(setup_negative_fixture)
def test_negative():
    assert isinstance(stats['test_neg']['time'], float)
    assert isinstance(stats['test_neg']['kstones'], float)
    assert isinstance(stats['test_neg']['memory'], numbers.Real)
    assert stats['test_neg']['time'] > 0
    assert stats['test_neg']['kstones'] < kpystones / 100
    assert stats['test_neg']['memory'] >= 0


@with_setup(setup_memory_fixture)
def test_check_memory():
    assert isinstance(stats['test_neg']['time'], float)
    assert isinstance(stats['test_neg']['kstones'], float)
    assert isinstance(stats['test_neg']['memory'], numbers.Real)
    assert stats['test_neg']['time'] > 0
    assert stats['test_neg']['kstones'] > 0

    is_pypy = '__pypy__' in sys.builtin_module_names
    op = operator.ge if is_pypy else operator.gt
    assert op(stats['test_neg']['memory'], 0)


def test_cpu_info_smoke():
    if platform.system() == 'Windows':
        cpu_info_stub = './tests/stubs/cpu'
        cpu = CpuInfo(cpu_info_stub)
    else:
        cpu = CpuInfo()
    assert cpu.__str__()
    assert cpu.__repr__()
    assert cpu.dict().keys()
    assert cpu.search('CPU Mhz')


def test_mem_info_smoke():
    if platform.system() == 'Windows':
        mem_info_stub = './tests/stubs/mem'
        mem = MemInfo(mem_info_stub)
    else:
        mem = MemInfo()
    assert mem.__str__()
    assert mem.__repr__()
    assert mem.dict().keys()
    assert mem.search('Swap')
    assert mem.get('Inactive(anon)')


def test_cpu_info_detailed():
    cpu_info_stub = './tests/stubs/cpu'
    cpu = CpuInfo(cpu_info_stub)
    content = '\n'.join(line.strip() for line in open(cpu_info_stub, 'r'))
    assert cpu.__str__() == cpu.__repr__() == content
    assert cpu.dict().keys()
    assert int(cpu.dict()['1']['cpu cores']) == 2
    assert len(cpu.search('CPU Mhz')) == 4


def test_mem_info_detailed():
    mem_info_stub = './tests/stubs/mem'
    mem = MemInfo(mem_info_stub)
    content = '\n'.join(line.strip() for line in open(mem_info_stub, 'r'))
    assert mem.__str__() == mem.__repr__() == content
    assert mem.dict().keys()
    assert mem.dict()['Active(anon)'] == '1794356 kB'
    assert len(mem.search('Swap')) == 3
    assert mem.get('Inactive(anon)') == 492656


def test_chrome_profiler_smoke():
    profiler = GProfiler()
    profiler.start()
    my_expensive_code()
    profiler.stop()

    assert isinstance(profiler.output(), str)
    assert profiler.output() != json.dumps({})
    assert 'startTime' in profiler.output()
    assert 'endTime' in profiler.output()
    assert 'timestamps' in profiler.output()
    assert 'samples' in profiler.output()
    assert 'head' in profiler.output()


def test_node_smoke():
    root = Node('head', 1)
    id_gen = GProfiler()._id_generator
    root.add(['1', '2'], id_gen)
    data = root.serialize()

    assert isinstance(data, dict)
    assert 'functionName' in data
    assert 'hitCount' in data
    assert 'children' in data
    assert 'scriptId' in data
    assert 'lineNumber' in data
    assert 'columnNumber' in data
    assert 'deoptReason' in data
    assert 'id' in data
    assert 'callUID' in data
    assert isinstance(data['children'], list)


def test_chrome_profiler_context_mgr_smoke():
    with GProfiler():
        my_expensive_code()

    filename = './pybenchmark_%s_.cpuprofile' % os.getpid()
    assert os.path.isfile(filename)
