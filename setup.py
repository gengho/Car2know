"""A setuptools based setup module.
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.MD'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='car2know',

    version='1.0.0',

    description='analyse the influx and outflux of Car2Go in different blocks in Seattle',
    long_description=long_description,

    url='https://github.com/gengho/Car2know',

    author='Geng Zeng, Yuxuan Cheng, He Zhe, Xiasen Wang',

    author_email='genguni@gmail.com, yxcheng@uw.edu,wxiasen@gmail.com,zhehe@uw.edu',

    license='MIT',

    classifiers=[

        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Data analysis and visualization',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='car2go data visualization geoinformatics',

    packages=find_packages(exclude=['Car2know', 'docs', 'data']),

    install_requires=['shapely','geopandas','pandas','pysal','scipy','numpy','urllib2'],


)
"""
Ref:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
