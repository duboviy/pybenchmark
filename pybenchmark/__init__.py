"""
Performance utility functional used in performance tests.

When measuring execution time, the result depends on the computer hardware.
To be able to produce a universal measure, the simplest way is to benchmark the
speed of a fixed sequence of code and calculate a ratio out of it. From there, the time
taken by a function can be translated to a universal value that can be compared on
any computer. Python provides a benchmark utility in its test package that measures the duration
of a sequence of well-chosen operations.
"""
from test import pystone
from time import time


# The result is a number of pystones per second the computer is able to perform,
# and the time used to perform the benchmark, result depends on the hardware.
BENCHTIME, PYSTONES = pystone.pystones()
KPYSTONES = PYSTONES / 1000.0
PERFORMANCE_STATS = {}


def duration(name='stats', stats=PERFORMANCE_STATS):
    def _duration(function):
        def __duration(*args, **kw):
            start_time = time()
            try:
                return function(*args, **kw)
            finally:
                total = time() - start_time
                kstones = _seconds_to_kpystones(total)
                stats[name] = {'total_time': total, 'kilo_stones': kstones}

        return __duration

    return _duration


def _seconds_to_kpystones(seconds):
    """ Return pystones amount of time performing operations. """
    return (PYSTONES * seconds) / 1000
