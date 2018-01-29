# -*- coding: utf-8 -*-
#
import codecs
import os
from setuptools import setup, find_packages

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, 'cplot', '__about__.py'), 'rb') as f:
    exec(f.read(), about)


def read(fname):
    try:
        content = codecs.open(
            os.path.join(os.path.dirname(__file__), fname),
            encoding='utf-8'
            ).read()
    except Exception:
        content = ''
    return content


setup(
    name='cplot',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=find_packages(),
    description='plotting tools for complex-valued functions',
    long_description=read('README.rst'),
    url='https://github.com/nschloe/cplot',
    download_url='https://pypi.python.org/pypi/cplot',
    license=about['__license__'],
    platforms='any',
    install_requires=[
        'numpy',
        'pipdate',
        ],
    classifiers=[
        about['__status__'],
        about['__license__'],
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering'
        ]
    )
