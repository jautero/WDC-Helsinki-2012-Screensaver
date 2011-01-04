"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app, glob

plist = dict(
    NSPrincipalClass='WDCSaver',
)

setup(
    plugin=['wdchelsinki2012.py'],
    py_modules=[],
    options=dict(py2app=dict(
        extension='.saver',
        plist=plist,
    )),
)
