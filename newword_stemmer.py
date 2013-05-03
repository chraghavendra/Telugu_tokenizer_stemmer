# -*- coding: utf-8 -*-

stems = []
suffixes = []

import math



import codecs

f = codecs.open('stem_suffix_1L', 'r', encoding='utf-8')


for line in f:
	(key, val) = line.split()
	stems += key
	suffixes += val

stems_set = [e for e in set(stems)]
suffixes_set = [e for e in set(suffixes)]


freq_stems = {}
freq_suffixes = {}

for stem in stems_set:
    freq_stems[stem] = stems.count(stem)
    #print freq_stems[stem]

for suffix in suffixes_set:
    freq_suffixes[suffix] = suffixes.count(suffix)
    #print freq_suffixes[suffix]



optimal_stem = ''
optimal_suffix = ''


def get_heuristic_values(word):

    heuristic_values = []

    max_heuristic_value = 0
    optimal_stem = ''
    optimal_suffix = ''

    if len(word) <= 2:
        return optimal_stem, optimal_suffix

    #print 'length '+str(len(word))
    for i in range(2, len(word)):
        #print word[:i]
        stem_count = 0
        suffix_count = 0
        if freq_stems.has_key(word[:i]):
            stem_count = freq_stems[word[:i]]
        #print word[i:]
        if freq_suffixes.has_key(word[i:]):
            suffix_count = freq_suffixes[word[i:]]

        if stem_count==0 and suffix_count==0:
            h_value = 0
        elif stem_count==0:
            h_value = (len(word) - i) * math.log(suffix_count)
        elif suffix_count==0:
            h_value = i * math.log(stem_count)
        else :
            h_value = i * math.log(stem_count) +  (len(word) - i) * math.log(suffix_count)

        if h_value >= max_heuristic_value:
            max_heuristic_value = h_value
            optimal_stem = word[:i]
            optimal_suffix = word[i:]

        heuristic_values.append(h_value)

    return optimal_stem, optimal_suffix


suffix_file = codecs.open('final_suffixes.txt', 'r', encoding='utf-8')

finalsuffixes = []

for line in suffix_file:
    finalsuffixes.append(line.replace(u"\n",""))

def get_stem_suffix(word):

    optimal_stem = word
    optimal_suffix = ''

    if len(word) <= 2:
        return optimal_stem, optimal_suffix

    #print 'length '+str(len(word))
  
    for i in range(2, len(word)):
  
        if word[i:] in finalsuffixes:
            optimal_stem = word[:i]
            optimal_suffix = word[i:]
            return optimal_stem, optimal_suffix

    return optimal_stem, optimal_suffix



inputfile = codecs.open('telugu_demo.txt', 'r', encoding='utf-8')
#newword = u'అతడొకసారి'
#print newword
for newword in inputfile:
    word = newword.replace(u"\n","")
    #print len(word)
    optimal_stem, optimal_suffix = get_stem_suffix(word)
    print optimal_stem.encode('utf-8')+"       "+optimal_suffix.encode('utf-8') 
