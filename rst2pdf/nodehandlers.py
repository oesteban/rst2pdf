# -*- coding: utf-8 -*-
# See LICENSE.txt for licensing terms
#$URL$
#$Date$
#$Revision$

# Import all node handler modules here.
# The act of importing them wires them in.

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
from rst2pdf import genelements
from rst2pdf import genpdftext

#sphinxnodes needs these
from rst2pdf.genpdftext import NodeHandler, FontHandler, HandleEmphasis

# createpdf needs this
nodehandlers = NodeHandler()
