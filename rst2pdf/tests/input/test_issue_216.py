#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus.doctemplate import Indenter
from reportlab.platypus.flowables import *
from reportlab.platypus.xpreformatted import *
from reportlab.lib.styles import getSampleStyleSheet
from copy import copy

def go():
        Story=[]
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate("issue216.pdf")
        
        knstyle=copy(styles['Normal'])
        heading=Paragraph('A heading at the beginning of the document',knstyle)
        heading.keepWithNext=True
        content= XPreformatted('This is the content\n'*120,styles['Normal'])
        
        Story=[heading,content]
        doc.build(Story)

go()
