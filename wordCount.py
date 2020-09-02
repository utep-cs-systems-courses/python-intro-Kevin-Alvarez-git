#! /usr/bin/env python3

import re

file_name = 'declaration.txt'
declaration = open(file_name, 'r')
file = declaration.read()
declaration.close()
file = file.lower()

words = re.split(r'[\W]+', file) # Tokenize each word ignoring special symbols
del(words[-1]) # Remove empty token caused by previous instruction

dic = {} # Dictionary to map words to the # of their occurrences

# Count the number of times each word appears
for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

sorted_list = sorted(dic.keys())

# Create new file and write into it
# each word and its number of occurrences
new_file_name = "myOutput.txt"
new_file = open(new_file_name, 'w')

for word in sorted_list:
    new_file.write(word + ' ' + str(dic[word]) + '\n')

new_file.close()