import re
import sys
# This is to find the highest frequency words appeared in the book
file_name = sys.argv[1]
f = open(file_name,'r+')
top_words_file = open('thousand_most_common.txt','r+')

words = [x for y in [l.split() for l in f.readlines()] for x in y]
if "I" and "to"in words:
	print True
else:
	print False         

top_words_list = top_words_file.read().splitlines()
if "I" and "to" in top_words_list:
	print True 
else:
	print False

recovery_words = [x for x in words if x not in top_words_list]

print sorted([(w, recovery_words.count(w)) for w in set(recovery_words)], key = lambda x:x[1], reverse=True)[:25]

