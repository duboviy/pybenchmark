""" A benchmark utility used in speed/performance tests. """
import time
import sys
from test import pystone    # native python-core "PYSTONE" Benchmark Program

# A Guppy-PE Primer (http://guppy-pe.sourceforge.net) is a third party framework that provides a
# memory profiler called Heap, among other features.
# Installed by requirments.txt. Custom installation >>> pip install guppy
# from guppy import hpy

# same condition in timeit (getting wall-time -> not process time)
timer = time.clock if sys.platform == 'win32' else time.time


# The result is a number of pystones per second the computer is able to perform,
# and the time used to perform the benchmark, result depends on the hardware.
BENCHTIME, PYSTONES = pystone.pystones()
KPYSTONES = PYSTONES / 1000.0
STATS = {}

# _INIT_MEM_SIZE = 12     # 12 corresponds to the initial memory size after a setref call


def profile(name='stats', stats=STATS):
    """Calculates a duration and a memory size."""
    def _profile(function):
        def __profile(*args, **kw):
            start_time = timer()
            # profiler = hpy()
            # profiler.setref()
            # start = profiler.heap().size + _INIT_MEM_SIZE
            try:
                return function(*args, **kw)
            finally:
                total = timer() - start_time
                kstones = _seconds_to_kpystones(total)
                # memory = profiler.heap().size - start
                stats[name] = {'time': total,
                               'kstones': kstones}
                               # 'memory': memory}
        return __profile
    return _profile


def _seconds_to_kpystones(seconds):
    """ Return pystones amount of time performing operations. """
    return (PYSTONES * seconds) / 1000


if __name__ == '__main__':
    """ Example of usage. """
    some_code = lambda: time.sleep(0.1)   # callable that will be decorated and measured
    decorated = profile('example_of_usage')(some_code)  # a la-carte decoration
    return_value = decorated()            # actual run/call of decorated callable
    print(STATS)
