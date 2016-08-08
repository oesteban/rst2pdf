# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
import cx_Freeze
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"
includes = [ "sip", 
             "PyQt4.QtXml"
]
packages = [ "pygments" , 
             "pygments.lexers", 
             "pygments.styles", 
             "docutils.writers",
             "docutils.readers",
             "docutils.languages",
]
excludes = [ "matplotlib",
             "PythonMagick",
             "sphinx",
             "pyPdf"
]

executables = [
        cx_Freeze.Executable("main.py", 
                             base = base, )
]

includeFiles = [
    ("../rst2pdf/styles", "styles"),
]

options = dict(
    #copyDependentFiles = True,
    include_files = includeFiles,
    includes = includes, 
    excludes = excludes,
    packages = packages)
    
cx_Freeze.setup(
        name = "bookrest",
        version = "0.1",
        description = "A rst2pdf GUI",
        executables = executables,
        options = dict(build_exe = options)
)
