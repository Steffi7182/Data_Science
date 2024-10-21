print("Name:Steffi Antony")
print("Reg no:SJC23MCA-2054")
from nltk import ngrams
sentence = 'I reside in India'
n = 3
trigrams = ngrams(sentence.split(),n)
for grams in trigrams:
    print(grams)