<h1><img src="https://raw.githubusercontent.com/duboviy/pybenchmark/master/logo.png" height=85 alt="logo" title="logo"> pybenchmark</h1>

by [Eugene Duboviy](https://duboviy.github.io/)

[![Build Status](https://travis-ci.org/duboviy/pybenchmark.svg?branch=master)](https://travis-ci.org/duboviy/pybenchmark) [![CircleCI](https://circleci.com/gh/duboviy/pybenchmark.svg?style=svg)](https://circleci.com/gh/duboviy/pybenchmark) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3a7bdeaac57c431ab1263fcd5f19e4a9)](https://www.codacy.com/app/dubovoy/pybenchmark?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duboviy/pybenchmark&amp;utm_campaign=Badge_Grade) [![PyPI](https://img.shields.io/pypi/v/pybenchmark.svg)](https://pypi.python.org/pypi/pybenchmark) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/3a7bdeaac57c431ab1263fcd5f19e4a9)](https://www.codacy.com/app/dubovoy/pybenchmark?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duboviy/pybenchmark&amp;utm_campaign=Badge_Coverage) [![Code Health](https://landscape.io/github/duboviy/pybenchmark/master/landscape.svg?style=flat)](https://landscape.io/github/duboviy/pybenchmark/master) [![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/duboviy/pybenchmark/) [![PRs & Issues Welcome](https://img.shields.io/badge/PRs%20&%20Issues-welcome-brightgreen.svg)](https://github.com/duboviy/pybenchmark/pulls) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/duboviy/pybenchmark/)

A benchmark utility used in speed / performance tests.

## Summary

When measuring execution time, the result depends on the computer hardware.
To be able to produce a universal measure, the simplest way is to benchmark the
speed of a fixed sequence of code and calculate a ratio out of it. From there, the time
taken by a function can be translated to a universal value that can be compared on
any computer. Python provides a benchmark utility in its test package that measures the duration
of a sequence of well-chosen operations. pybenchmark designed to provide a simple 
and pythonic way to get performance data.

## Current features

* Simple usage workflow
* Decorator for profiling
* A la carte usage of decorator in place
* Provide a simple way to get CPU and memory details information

## Installation:

Install from PyPI:
```
$ pip install pybenchmark
```
Or using alternative command:
```
pip install https://github.com/duboviy/pybenchmark/archive/master.zip
```
Or from source use:
```
$ python setup.py install
```

## Supported python versions

  * 2.7
  * 3.3
  * 3.4
  * 3.5
  * 3.6
  * PyPy

## PyPI

* [Package](https://pypi.python.org/pypi/pybenchmark)
* [Documentation](https://pythonhosted.org/pybenchmark/)

## Basic usage examples

You can use profile decorator to wrap your code:

```python
from pybenchmark import profile

@profile()
def some_code():
    time.sleep(0.5)

some_code()
print(stats)
{'stats':  {'kstones': 0.50012803077697754, 'time': 24.278059746455238, 'memory': 0}
```

Also you can use decorator à la carte,
if you don't want to edit/disturb your source code (for example, when writing tests):

```python
import pybenchmark

eat_cpu_time = lambda: 2**100000000

# using decorator à la carte below
eat_it = pybenchmark.profile('you bad boy!')(eat_cpu_time)
please = eat_it()

pybenchmark.stats
{'you bad boy!': {'kstones': 14.306935999128555, 'time': 0.30902981758117676, 'memory': 8096}}
```

You can use module for visualizing Python code profiles using the Chrome developer tools:

```python
from pybenchmark import GProfiler

profiler = GProfiler()
profiler.start()
my_expensive_code()
profiler.stop()

with open('my.cpuprofile', 'w') as f:
    f.write(profiler.output())
```

Or you can use context manager:

```python
with GProfiler() as profiler:
    my_expensive_code()

# File with name './pybenchmark_%s_.cpuprofile' % os.getpid() would be created
```

Then load json file into chrome developer tools timeline.
To get the timeline chart load the file into Profiles tool from Chrome Dev Tools.
There is a "Load" button just under the list of profiles.
Then timeline-chart can be obtained by changing Heavy(Bottom Up) option to Chart.
<img src="http://i.stack.imgur.com/To8Nw.png" alt="&quot;Load&quot; button on the Profiles tab in Chrome DevTools">
You can use it with or without gevent framework.

You can get CPU machine details information (on LINUX-based systems): 

```
>>> from pybenchmark import CpuInfo
>>> cpu = CpuInfo()
>>> cpu
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
stepping	: 7
microcode	: 0x28
cpu MHz		: 1600.257
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
bogomips	: 6784.56
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
stepping	: 7
microcode	: 0x28
cpu MHz		: 1600.523
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 1
cpu cores	: 2
apicid		: 2
initial apicid	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
bogomips	: 6784.56
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 2
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
stepping	: 7
microcode	: 0x28
cpu MHz		: 1595.476
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 2
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
bogomips	: 6784.56
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 3
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
stepping	: 7
microcode	: 0x28
cpu MHz		: 1599.062
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 1
cpu cores	: 2
apicid		: 3
initial apicid	: 3
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
bogomips	: 6784.56
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
```

Return output as dict:

```
>>> cpu.dict()
{
    "1": {
        "cpu cores": "2",
        "bogomips": "6784.56",
        "core id": "1",
        "apicid": "2",
        "fpu_exception": "yes",
        "stepping": "7",
        "cache_alignment": "64",
        "clflush size": "64",
        "microcode": "0x28",
        "cache size": "3072 KB",
        "cpuid level": "13",
        "fpu": "yes",
        "model name": "Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz",
        "siblings": "4",
        "physical id": "0",
        "address sizes": "36 bits physical, 48 bits virtual",
        "cpu family": "6",
        "vendor_id": "GenuineIntel",
        "wp": "yes",
        "power management": "",
        "flags": "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid",
        "cpu MHz": "1683.398",
        "model": "42",
        "processor": "1",
        "initial apicid": "2"
    },
    "0": {
        "cpu cores": "2",
        "bogomips": "6784.56",
        "core id": "0",
        "apicid": "0",
        "fpu_exception": "yes",
        "stepping": "7",
        "cache_alignment": "64",
        "clflush size": "64",
        "microcode": "0x28",
        "cache size": "3072 KB",
        "cpuid level": "13",
        "fpu": "yes",
        "model name": "Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz",
        "siblings": "4",
        "physical id": "0",
        "address sizes": "36 bits physical, 48 bits virtual",
        "cpu family": "6",
        "vendor_id": "GenuineIntel",
        "wp": "yes",
        "power management": "",
        "flags": "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid",
        "cpu MHz": "1601.187",
        "model": "42",
        "processor": "0",
        "initial apicid": "0"
    },
    "3": {
        "cpu cores": "2",
        "bogomips": "6784.56",
        "core id": "1",
        "apicid": "3",
        "fpu_exception": "yes",
        "stepping": "7",
        "cache_alignment": "64",
        "clflush size": "64",
        "microcode": "0x28",
        "cache size": "3072 KB",
        "cpuid level": "13",
        "fpu": "yes",
        "model name": "Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz",
        "siblings": "4",
        "physical id": "0",
        "address sizes": "36 bits physical, 48 bits virtual",
        "cpu family": "6",
        "vendor_id": "GenuineIntel",
        "wp": "yes",
        "power management": "",
        "flags": "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid",
        "cpu MHz": "1612.476",
        "model": "42",
        "processor": "3",
        "initial apicid": "3"
    },
    "2": {
        "cpu cores": "2",
        "bogomips": "6784.56",
        "core id": "0",
        "apicid": "1",
        "fpu_exception": "yes",
        "stepping": "7",
        "cache_alignment": "64",
        "clflush size": "64",
        "microcode": "0x28",
        "cache size": "3072 KB",
        "cpuid level": "13",
        "fpu": "yes",
        "model name": "Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz",
        "siblings": "4",
        "physical id": "0",
        "address sizes": "36 bits physical, 48 bits virtual",
        "cpu family": "6",
        "vendor_id": "GenuineIntel",
        "wp": "yes",
        "power management": "",
        "flags": "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid",
        "cpu MHz": "1600.125",
        "model": "42",
        "processor": "2",
        "initial apicid": "1"
    }
}
```

Search (is case insensitive):

```
>>> cpu.search('CPU Mhz')
['cpu MHz\t\t: 1599.062\n', 'cpu MHz\t\t: 1600.125\n', 'cpu MHz\t\t: 1598.398\n', 'cpu MHz\t\t: 1601.320\n']
```

You can also get memory machine details information (on LINUX-based systems):

```
>>> from pybenchmark import MemInfo
>>> mem = MemInfo()
>>> mem
MemTotal:        8092460 kB
MemFree:          499880 kB
MemAvailable:    5454920 kB
Buffers:          219088 kB
Cached:          4980040 kB
SwapCached:         7576 kB
Active:          5647392 kB
Inactive:        1628708 kB
Active(anon):    1794356 kB
Inactive(anon):   492656 kB
Active(file):    3853036 kB
Inactive(file):  1136052 kB
Unevictable:         200 kB
Mlocked:             200 kB
SwapTotal:      16776188 kB
SwapFree:       16639112 kB
Dirty:               172 kB
Writeback:             0 kB
AnonPages:       2070440 kB
Mapped:           204800 kB
Shmem:            210036 kB
Slab:             247884 kB
SReclaimable:     219356 kB
SUnreclaim:        28528 kB
KernelStack:        4144 kB
PageTables:        11904 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    20822416 kB
Committed_AS:    3317504 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      362844 kB
VmallocChunk:   34359347296 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:       83644 kB
DirectMap2M:     8202240 kB
```

Return output as dict:

```
>>> mem.dict()
{
	"WritebackTmp": "0 kB",
	"SwapTotal": "16776188 kB",
	"Active(anon)": "1794356 kB",
	"SwapFree": "16639112 kB",
	"DirectMap4k": "83644 kB",
	"KernelStack": "4144 kB",
	"MemFree": "499880 kB",
	"HugePages_Rsvd": "0",
	"Committed_AS": "3317504 kB",
	"SUnreclaim": "28528 kB",
	"NFS_Unstable": "0 kB",
	"VmallocChunk": "34359347296 kB",
	"Writeback": "0 kB",
	"Inactive(file)": "1136052 kB",
	"MemTotal": "8092460 kB",
	"VmallocUsed": "362844 kB",
	"HugePages_Free": "0",
	"AnonHugePages": "0 kB",
	"Shmem": "210036 kB",
	"AnonPages": "2070440 kB",
	"Active": "5647392 kB",
	"Inactive(anon)": "492656 kB",
	"HugePages_Total": "0",
	"Hugepagesize": "2048 kB",
	"Cached": "4980040 kB",
	"SwapCached": "7576 kB",
	"VmallocTotal": "34359738367 kB",
	"Dirty": "172 kB",
	"Mapped": "204800 kB",
	"Unevictable": "200 kB",
	"SReclaimable": "219356 kB",
	"MemAvailable": "5454920 kB",
	"Slab": "247884 kB",
	"DirectMap2M": "8202240 kB",
	"HugePages_Surp": "0",
	"Bounce": "0 kB",
	"Inactive": "1628708 kB",
	"PageTables": "11904 kB",
	"HardwareCorrupted": "0 kB",
	"CommitLimit": "20822416 kB",
	"Mlocked": "200 kB",
	"Buffers": "219088 kB",
	"Active(file)": "3853036 kB"
}
```

Search (is case insensitive):

```
>>> mem.search('Swap')
['SwapCached:         7576 kB\n', 'SwapTotal:      16776188 kB\n', 'SwapFree:       16639112 kB\n']
```

Get memory usage as int (is case sensitive):

```
>>> mem.get('Inactive(anon)')
492656
```


## License

**MIT** licensed library. See [LICENSE.txt](LICENSE.txt) for details.

## Contributing

If you have suggestions for improving the pybenchmark, please [open an issue or
pull request on GitHub](https://github.com/duboviy/pybenchmark/).

## Badges

[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/duboviy/pybenchmark/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/duboviy/pybenchmark/) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](https://github.com/duboviy/pybenchmark/) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](https://github.com/duboviy/pybenchmark/)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/duboviy/pybenchmark/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://github.com/duboviy/pybenchmark/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](https://github.com/duboviy/pybenchmark/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://github.com/duboviy/pybenchmark/)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/duboviy/pybenchmark/)


