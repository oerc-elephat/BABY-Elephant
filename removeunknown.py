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
    outputfile = open(data_dir + 'output2.txt', 'w')
    lines = check.readlines()
    

    countwork = 0
    for line in lines:
        if re.match("^\s*$", line):
            continue
        line = line.replace('\t','|')
        line = line.split('|')
        
        if line[2] != 's.n\n' and line[2] !='s.n.\n' and not re.match("s.n.*", line[2]):
            outputfile.write(line[0]+'|'+line[1]+ '|'+ line[2]+'\n')
            print line[2]
        
            if re.match("work*", line[0]):
                countwork += 1
    print countwork  #total 20726 with publisher information
    

    check.close()
    outputfile.close()

if __name__ == "__main__":
    main()