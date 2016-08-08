# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY

def go():
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate("phello.pdf")
    style = styles['Normal']
    style.alignment=TA_JUSTIFY
    p1 = Paragraph('''PADDING PADDING PADDING PADDING PADDING PADDING The computer will always be better than you at parsing SQL
and the bad guys have years of experience finding and using <a href="http://en.wikipedia.org/wiki/SQL_injection" color="navy">SQL
injection attacks</a><a name="sql-injection-attacks"/> in
ways you never even thought possible.''', style)
    doc.build([p1,])

go()
