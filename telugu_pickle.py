# -*- coding: utf-8 -*-

from nltk.corpus import IndianCorpusReader
import nltk.tokenize.punkt
import codecs


print "passing given text to PunktSentenceTokenizer... "

tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

tokenizer.train(codecs.open('telugucorpus.txt', 'rw', encoding='utf-8'))

print "training completed !"

# Dump pickled tokenizer
import pickle

out = open("telugu.pickle","wb")

print "Writing into pickle file... telugu.pickle"
pickle.dump(tokenizer, out)
print "pickle file generated !"
out.close()