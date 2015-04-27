import re
from collections import Counter
from operator import itemgetter
import csv

with open('input.txt') as f:
    passage = f.read()
words = re.findall(r'\w+', passage) #This finds words in the document
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)
word_counts.most_common()
wordCounts=sorted(word_counts.items())
print wordCounts
csvfile = "output.csv"
#Assuming wordCounts is a flat list
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in wordCounts:
        writer.writerow([val])  
