#!/usr/bin/env python
import sys, string
import re
import nltk
import nltk.data
from nltk.tokenize import word_tokenize

def main():
    print "Start"
    
    data_dir = "/Users/Brishti/Documents/Internships/scripts/"

    check = open(data_dir + 'output.txt', 'r')
    # outputfile = open(data_dir + 'output.txt', 'w')
    
    num = 0
    for line in check:
        if re.match("^\s*$", line):
            continue
        line = line.replace('\t','|')
        line = line.split('|')
        
        if line[2]=='s.n\n' or line[2]=='s.n.\n':
            num += 1
    print num
        
        # for char in '[]"?!':
#             line[2] = line[2].replace(char, '')
#             line[2] = re.sub('\.*,\s*$', '', line[2])
        # print line[2]
        # outputfile.write(line[0]+'|'+line[1]+ '|'+ line[2]+'\n')

    check.close()
    # outputfile.close()

if __name__ == "__main__":
    main()