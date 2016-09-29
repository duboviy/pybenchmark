""" A benchmark utility used in speed/performance tests. """
import os
import sys
import time
from test import pystone    # native python-core "PYSTONE" Benchmark Program

import psutil


# The result is a number of pystones per second the computer is able to perform,
# and the time used to perform the benchmark, result depends on the hardware.
benchtime, pystones = pystone.pystones()
kpystones = pystones / 1000.0
stats = {}


# pylint: disable-msg=W0102
def profile(name='stats', _stats=stats):
    """Calculates a duration and a memory size."""
    def _profile(function):
        def __profile(*args, **kw):
            start_time = _get_time()
            start_memory = _get_memory_usage()
            try:
                return function(*args, **kw)
            finally:
                total = _get_time() - start_time
                kstones = _seconds_to_kpystones(total)
                memory = _get_memory_usage() - start_memory
                _stats[name] = {'time': total,
                                'kstones': kstones,
                                'memory': memory}
        return __profile
    return _profile


def _get_time():
    """ Return wall-time -> not process time (same condition in timeit). """
    timer = time.clock if sys.platform == 'win32' else time.time
    return timer()


def _seconds_to_kpystones(seconds):
    """ Return pystones amount of time performing operations. """
    return (pystones * seconds) / 1000


def _get_memory_usage():
    """ Return the memory resident set size (top->RES) usage in bytes. """
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss
    return mem
