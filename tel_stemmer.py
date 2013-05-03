# -*- coding: utf-8 -*-

from nltk.corpus import IndianCorpusReader

import math

def get_stems(word):


    stems = []
    for i in range(2, len(word)):
        stems.append(word[:i])
    return stems


def get_suffixes(word):

    suffixes = []
    for i in range(2, len(word)):
        suffixes.append(word[i:])
    return suffixes

telugu_corpus = IndianCorpusReader('', 'telugu_word1.txt')
telugu_words = telugu_corpus.words()

#telugu_words = ['Rakesh', 'Balu', 'Raghavendra', 'Raghu', 'Raveendhra', 'Raghav']

words = {}

for word in telugu_words:

    stems = get_stems(word)
    suffixes = get_suffixes(word)

    words[word] = { 'stems': stems, 'suffixes': suffixes }

stems = []
suffixes = []


#adding lists
for word in words:
    stems += words[word]['stems']
    suffixes += words[word]['suffixes']

stems_set = [e for e in set(stems)]
suffixes_set = [e for e in set(suffixes)]

freq_stems = {}
freq_suffixes = {}

for stem in stems_set:
    freq_stems[stem] = stems.count(stem)

for suffix in suffixes_set:
    freq_suffixes[suffix] = suffixes.count(suffix)

#print "\nfrequency of stems", freq_stems

#print "\nfrequency of suffixes", freq_suffixes

# for word in words:

#     freq_optimal_stem = 0
#     freq_optimal_suffix = 0


#     for stem in words[word]['stems']:
#         if freq_stems[stem] > freq_optimal_stem:
#             optimal_stem = stem
#             freq_optimal_stem = freq_stems[stem]

#     for suffix in words[word]['suffixes']:
#       if freq_suffixes[suffix] > freq_optimal_suffix:
#           optimal_suffix = suffix
#           freq_optimal_stem = freq_suffixes[suffix]

#     heuristic_values = []

def get_heuristic_values(word):

    heuristic_values = []

    max_heuristic_value = 0
    optimal_stem = ''
    optimal_suffix = ''

    if len(word) <= 2:
        return heuristic_values, optimal_stem, optimal_suffix

    for i in range(2, len(word)):
        h_value = i * math.log(freq_stems[word[:i]]) +  (len(word) - i) * math.log(freq_suffixes[word[i:]])

        if h_value >= max_heuristic_value:
            max_heuristic_value = h_value
            optimal_stem = word[:i]
            optimal_suffix = word[i:]

        heuristic_values.append(h_value)

    return heuristic_values, optimal_stem, optimal_suffix


for i in range(2):

    #print i
    optimal_stems =[]
    optimal_suffixes = []

    for word in words:

        heuristic_values, optimal_stem, optimal_suffix = get_heuristic_values(word)
        words[word]['heuristic_values'] = heuristic_values
        words[word]['optimal_stem'] = optimal_stem
        words[word]['optimal_suffix'] = optimal_suffix
        #adding an element to a list
        optimal_stems.append(optimal_stem)
        optimal_suffixes.append(optimal_suffix)

    stems_set = [e for e in set(optimal_stems)]
    suffixes_set = [e for e in set(optimal_suffixes)]

    for stem in stems_set:
        freq_stems[stem] = optimal_stems.count(stem)

    for suffix in suffixes_set:
        freq_suffixes[suffix] = optimal_suffixes.count(suffix)



#print "\n\n"

# word = { 'Raghavendra': 
#             {
#                 'optimal_suffix': 'avendra', 
#                 'heuristic_values': [ 1.6094379124341003, 
#                                         3.2188758248682006, 
#                                         3.295836866004329, 
#                                         4.394449154672439, 
#                                         3.4657359027997265, 
#                                         0.0, 
#                                         0.0, 
#                                         0.0, 
#                                         1.3862943611198906, 
#                                         0.6931471805599453
#                                     ], 
#                 'suffixes': ['aghavendra', 'ghavendra', 'havendra', 
#                                 'avendra', 'vendra', 'endra', 
#                                 'ndra', 'dra', 'ra', 'a'],
                
#                 'optimal_stem': 'Ragh',

#                 'stems': ['R', 'Ra', 'Rag', 'Ragh', 'Ragha', 'Raghav', 'Raghave', 'Raghaven', 'Raghavend', 'Raghavendr']
#             }
#         }


# for word in words:
#     print "\n\n"
#     print "word", word, '\n'
#     print 'stems', '\n', '\n'.join(words[word]['stems']), '\n'
#     print 'suffixes', '\n', '\n'.join(words[word]['suffixes']), '\n'
#     print 'optimal_stem ', words[word]['optimal_stem'], '\n'
#     print 'optimal_suffix', words[word]['optimal_suffix'], '\n' 
#     # print 'heuristic_values', words[word]['heuristic_values'], '\n'
#     print "\n\n"

 #for stem in optimal_stems:
#     print '\n', stem, len(unicode(stem)), '\n'

optimal_stems_suffixes = zip(optimal_stems, optimal_suffixes)

#print 'STEM_SUFFIXES'
for i in optimal_stems_suffixes:
    stem = i[0].encode('utf-8','replace')
    suffix = i[1].encode('utf-8','replace')
    print stem,'\t',suffix

#print '\n'.join(optimal_stems), '\n\n\n', '\n'.join(optimal_suffixes)