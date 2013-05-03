# -*- coding: utf-8 -*-

from nltk.tokenize import SpaceTokenizer

import sys

s = sys.argv[1].decode('utf-8')
dt = sys.argv[2]

#print "dt = "+dt

#python telugu_tokenizer.py "భారతదేశపు దక్షిణ \tసముద్ర \nప్రాంతంలో అది \n ‘పార్సన్స్ పిగ్మాలియన్’ ప్రదేశ"   ' 	'
tokens = []

if(dt == " "):
	tokens = SpaceTokenizer().tokenize(s)

#python telugu_tokenizer.py "భారతదేశపు దక్షిణ \tసముద్ర \nప్రాంతంలో అది \t ‘పార్సన్స్ పిగ్మాలియన్’ ప్రదేశ"   '\t'
from nltk.tokenize import TabTokenizer


if(dt == '\\t'):
	print "dt = "+dt
	s = s.replace(u'\\t','\t')
	tokens = TabTokenizer().tokenize(s)

#python telugu_tokenizer.py "భారతదేశపు దక్షిణ \tసముద్ర \nప్రాంతంలో అది \n ‘పార్సన్స్ పిగ్మాలియన్’ ప్రదేశ"   '\n'
from nltk.tokenize import LineTokenizer

if(dt == '\\n'):
	s = s.replace(u'\\n','\n')
	tokens = LineTokenizer(blanklines='discard').tokenize(s)


for token in tokens:
	print token.encode('utf-8','replace')

#print ', '.join(repr(x.encode('utf-8','replace')) for x in tokens)
#print type(tokens)(x.encode('utf-8') for x in tokens)

