
import setuptools

classifiers = ["Programming Language :: Python :: 3.5"]

setuptools.setup(
    name         = "justcache",
    version      = "0.0.1",
    author       = "Justus Schwabedal",
    author_email = "JSchwabedal@gmail.com",
    description  = ("Very simple python library for caching."),
    keywords     = "cache",
    url          = "https://github.com/jusjusjus/justcache",
    packages     = ['justcache'],
    include_package_data = True,
    classifiers	 = classifiers)
