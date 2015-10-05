import nltk
import re
import time

# text = 'Printed by Benjamin Took and John Crook, and are to be sold by Mary Crook & Andrew Crook'

def extract_ent():
    
    data_dir = "/Users/Brishti/Documents/Internships/scripts/"
    inputfile = open(data_dir + 'output3.txt', 'r')
    # outputfile = open(data_dir + 'entity.txt', 'w')
    
    for line in inputfile:
        # print("Looking at: " + line)
        if re.match("^\s*$", line):
            next
        line = line.split("|")
        # print("Length is: " + str(len(line)))
        # print line[2]
    
        
        for sent in nltk.sent_tokenize(line[2]):
            print("______")
            # print sent
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                # print nltk.pos_tag(nltk.word_tokenize(sent))
                print chunk
                #if hasattr(chunk, 'label') and chunk.label() == "PERSON":
                    # print chunk.leaves()
                    #print(line[0] + '|' +' '.join(c[0] for c in chunk.leaves())+'\n')
                    # outputfile.write(line[0] + '|' +' '.join(c[0] for c in chunk.leaves())+'\n')

    inputfile.close()
    # outputfile.close()

if __name__ == "__main__":
    extract_ent()