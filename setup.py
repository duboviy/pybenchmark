from distutils.core import setup
setup(
  name = 'pybenchmark',
  packages = ['pybenchmark'], # this must be the same as the name above
  version = '0.0.6',
  description = 'A benchmark utility used in performance tests.',
  author = 'Eugene Duboviy',
  author_email = 'eugene.dubovoy@gmail.com',
  url = 'https://github.com/duboviy/pybenchmark', # use the URL to the github repo
  download_url = 'https://github.com/duboviy/pybenchmark/tarball/0.0.6', # I'll explain this in a second
  keywords = ['benchmark', 'performance', 'testing'], # arbitrary keywords
  classifiers=[
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
  long_description="""
When measuring execution time, the result depends on the computer hardware.
To be able to produce a universal measure, the simplest way is to benchmark the speed of a fixed sequence
of code and calculate a ratio out of it. From there, the time taken by a function can be translated to a
universal value that can be compared on any computer. Python provides a benchmark utility in its test
package that measures the duration of a sequence of well-chosen operations.
pybenchmark designed to provide a simple and pythonic way to get performance data.
""",
  install_requires=[
    'psutil',
    'gevent',
  ],
)
