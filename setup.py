from distutils.core import setup
setup(
  name = 'pybenchmark',
  packages = ['pybenchmark'], # this must be the same as the name above
  version = '0.0.5',
  description = 'A benchmark utility used in performance tests.',
  author = 'Eugene Duboviy',
  author_email = 'eugene.dubovoy@gmail.com',
  url = 'https://github.com/duboviy/pybenchmark', # use the URL to the github repo
  download_url = 'https://github.com/duboviy/pybenchmark/tarball/0.0.5', # I'll explain this in a second
  keywords = ['benchmark', 'performance', 'testing'], # arbitrary keywords
  classifiers=[
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
  long_description=open('README.md').read(),
  install_requires=[
    'psutil',
    'gevent',
  ],
)
