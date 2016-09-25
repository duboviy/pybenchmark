import time
from nose.tools import with_setup

from pybenchmark import profile, STATS, KPYSTONES


POSITIVE_BENCHMARK_TIME = 0.1  # sec


def setup_positive_fixture():
    # callable that will be decorated and measured
    some_code = lambda: time.sleep(POSITIVE_BENCHMARK_TIME)
    decorated = profile('test')(some_code)  # a la-carte decoration
    return_value = decorated()  # actual run/call of decorated callable


def setup_negative_fixture():
    # callable that will be decorated and measured
    some_code = lambda: None
    decorated = profile('test_neg')(some_code)  # a la-carte decoration
    return_value = decorated()  # actual run/call of decorated callable


@with_setup(setup_positive_fixture)
def test_dict_keys():
    assert 'test' in STATS
    assert isinstance(STATS['test'], dict)
    assert 'time' in STATS['test']
    assert 'kstones' in STATS['test']
    # assert 'memory' in STATS['test']


@with_setup(setup_positive_fixture)
def test_dict_values():
    assert isinstance(STATS['test']['time'], float)
    assert isinstance(STATS['test']['kstones'], float)
    # assert isinstance(STATS['test']['memory'], float)
    assert STATS['test']['time'] > 0
    assert abs( (KPYSTONES * POSITIVE_BENCHMARK_TIME) - STATS['test']['kstones']) < 0.1
    # assert STATS['test']['memory'] > 0


@with_setup(setup_negative_fixture)
def test_negative():
    assert isinstance(STATS['test_neg']['time'], float)
    assert isinstance(STATS['test_neg']['kstones'], float)
    # assert isinstance(STATS['test_neg']['memory'], float)
    assert STATS['test_neg']['time'] > 0
    assert STATS['test_neg']['kstones'] < KPYSTONES / 1000
    # assert STATS['test_neg']['memory'] > 0
