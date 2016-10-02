""" A benchmark utility used in speed/performance tests. """
from os import getpid
from test import pystone            # native python-core "PYSTONE" Benchmark Program
from timeit import default_timer as timer

from psutil import Process


# The result is a number of pystones per second the computer is able to perform,
# and the time used to perform the benchmark, result depends on the hardware.
benchtime, pystones = pystone.pystones()
kpystones = pystones / 1000.0
stats = {}


# pylint: disable-msg=W0102
def profile(name='stats', _stats=stats):
    """Calculates a duration (wall clock time, not the CPU time) and a memory size."""
    def _profile(function):
        def __profile(*args, **kw):
            start_time = timer()
            start_memory = _get_memory_usage()
            try:
                return function(*args, **kw)
            finally:
                total = timer() - start_time
                kstones = _seconds_to_kpystones(total)
                memory = _get_memory_usage() - start_memory
                _stats[name] = {'time': total,
                                'kstones': kstones,
                                'memory': memory}
        return __profile
    return _profile


def _seconds_to_kpystones(seconds):
    """ Return pystones amount of time performing operations. """
    return (pystones * seconds) / 1000


def _get_memory_usage():
    """ Return the memory resident set size (top->RES) usage in bytes. """
    process = Process(getpid())
    mem = process.memory_info().rss
    return mem
