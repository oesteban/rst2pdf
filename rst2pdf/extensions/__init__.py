'''
This place-holder module makes the extensions directory
into a Python "package", so that external user-specific
modules can act as umbrella modules, and, for example:

import rst2pdf.extensions.vectorpdf_r2p

to bring in the PDF extension.
'''
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
