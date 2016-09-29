# pybenchmark

by [Eugene Duboviy](https://duboviy.github.io/)

[![Build Status](https://travis-ci.org/duboviy/pybenchmark.svg?branch=master)](https://travis-ci.org/duboviy/pybenchmark) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3a7bdeaac57c431ab1263fcd5f19e4a9)](https://www.codacy.com/app/dubovoy/pybenchmark?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duboviy/pybenchmark&amp;utm_campaign=Badge_Grade) [![PyPI](https://img.shields.io/pypi/v/pybenchmark.svg)](https://pypi.python.org/pypi/pybenchmark) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/3a7bdeaac57c431ab1263fcd5f19e4a9)](https://www.codacy.com/app/dubovoy/pybenchmark?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duboviy/pybenchmark&amp;utm_campaign=Badge_Coverage) [![Code Health](https://landscape.io/github/duboviy/pybenchmark/master/landscape.svg?style=flat)](https://landscape.io/github/duboviy/pybenchmark/master) [![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

A benchmark utility used in speed / performance tests.

## Why?

When measuring execution time, the result depends on the computer hardware.
To be able to produce a universal measure, the simplest way is to benchmark the
speed of a fixed sequence of code and calculate a ratio out of it. From there, the time
taken by a function can be translated to a universal value that can be compared on
any computer. Python provides a benchmark utility in its test package that measures the duration
of a sequence of well-chosen operations.

## Current features

* Simple usage workflow
* Decorator for profiling
* A la carte usage of decorator in place
* Work directly... no additional instalation

## Installation:

From source use:
```
$ python setup.py install
```
or install from PyPi:
```
$ pip install pybenchmark
```

## Examples

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

## Supported python versions

  * 2.7
  * 3.3
  * 3.4
  * 3.5
  * 3.6

## PyPI

* [Package](https://pypi.python.org/pypi/pybenchmark)
* [Documentation](https://pythonhosted.org/pybenchmark/)

## License

**MIT** licensed library. See [LICENSE.txt](LICENSE.txt) for details.

## Contributing

If you have suggestions for improving the pybenchmark, please [open an issue or
pull request on GitHub](https://github.com/duboviy/pybenchmark/).

## Badges

[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](http://forthebadge.com)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](http://forthebadge.com)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](http://forthebadge.com)


