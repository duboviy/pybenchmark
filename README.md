# pybenchmark

[![Build Status](https://travis-ci.org/duboviy/pybenchmark.svg?branch=master)](https://travis-ci.org/duboviy/pybenchmark) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3a7bdeaac57c431ab1263fcd5f19e4a9)](https://www.codacy.com/app/dubovoy/pybenchmark?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duboviy/pybenchmark&amp;utm_campaign=Badge_Grade) [![PyPI](https://img.shields.io/pypi/v/pybenchmark.svg)](https://pypi.python.org/pypi/pybenchmark) [![Coverage Status](https://coveralls.io/repos/boennemann/badges/badge.svg)](https://coveralls.io/r/boennemann/badges) [![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

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

## Instalation

```
pip install pybenchmark
```

## Examples

```python
>>> import pybenchmark
>>> eat_cpu_time = lambda: 2**100000000
>>> eat_it = pybenchmark.profile('you bad boy!')(eat_cpu_time)
>>> please = eat_it()
>>> profiler.stats
{'you bad boy!': {'kstones': 14.306935999128555, 'time': 0.30902981758117676}}
```

[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](http://forthebadge.com)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](http://forthebadge.com)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](http://forthebadge.com)
