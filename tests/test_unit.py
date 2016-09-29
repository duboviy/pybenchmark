import time
from nose.tools import with_setup
import numbers

from pybenchmark import profile, stats, kpystones, CpuInfo, MemInfo


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
    assert abs((kpystones * POSITIVE_BENCHMARK_TIME) - stats['test']['kstones']) < 0.2
    assert stats['test']['memory'] >= 0


@with_setup(setup_negative_fixture)
def test_negative():
    assert isinstance(stats['test_neg']['time'], float)
    assert isinstance(stats['test_neg']['kstones'], float)
    assert isinstance(stats['test_neg']['memory'], numbers.Real)
    assert stats['test_neg']['time'] > 0
    assert stats['test_neg']['kstones'] < kpystones / 1000
    assert stats['test_neg']['memory'] >= 0


@with_setup(setup_memory_fixture)
def test_check_memory():
    assert isinstance(stats['test_neg']['time'], float)
    assert isinstance(stats['test_neg']['kstones'], float)
    assert isinstance(stats['test_neg']['memory'], numbers.Real)
    assert stats['test_neg']['time'] > 0
    assert stats['test_neg']['kstones'] > 0
    assert stats['test_neg']['memory'] > 0


def test_cpu_info():
    cpu = CpuInfo()
    assert cpu.__str__
    assert cpu.__str__ == cpu.__repr__
    assert cpu.dict().keys()
    assert cpu.search('CPU Mhz')


def test_mem_info():
    mem = MemInfo()
    assert mem.__str__
    assert mem.__str__ == mem.__repr__
    assert mem.dict().keys()
    assert mem.search('Swap')
    assert mem.get('Inactive(anon)')
