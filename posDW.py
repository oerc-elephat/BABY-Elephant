import nltk
import re
import time

# text = 'Printed by Benjamin Took and John Crook, and are to be sold by Mary Crook & Andrew Crook'

def prepositionBeforePerson(chunks, ix):
    for i in range(ix-1, -1, -1): # for each chunk before this PERSON chunk in the sentence
        # print ": ", chunks[i]
        #if this chunk is a preposition:
            #return the preposition
        #print type(chunks[i][1])
        preposition = 0
        if len(chunks[i]) == 2 and chunks[i][1] == 'IN':
            preposition += 1
            print "The preposition is:", chunks[i][0]
            return chunks[i][0]
 
    return None      


def extract_ent():
    
    data_dir = "/Users/Brishti/Documents/Internships/scripts/"
    inputfile = open(data_dir + 'output3.txt', 'r')
    # outputfile1 = open(data_dir + 'publishedby.txt', 'w')
    # outputfile2 = open(data_dir + 'publishedfor.txt', 'w')
    
    for line in inputfile:
        # print("Looking at: " + line)
        if re.match("^\s*$", line):
            next
        line = line.split("|")
        # print("Length is: " + str(len(line)))
        # print line[2]
    
        
        for sent in nltk.sent_tokenize(line[2]):
            print("______")
            print line[0]
            # print sent
            chunks = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)))
            for ix, chunk in enumerate(chunks):
                print "chunk: ", chunk, ", index: ", ix
                if hasattr(chunk, 'label') and chunk.label() == "PERSON":
                    print "I have found a person chunk: ", chunk.leaves()
                    prep = prepositionBeforePerson(chunks, ix) #look back, hunting for prepositions
                    if prep:
                            # if this is FOR, you know it was printed FOR the person
                        if prep == 'by' or prep =='By':
                            print line[0] + ' ' + prep + ' ' + ' '.join(c[0] for c in chunk.leaves())
                            # outputfile1.write(line[0] + '|' + ' '.join(c[0] for c in chunk.leaves())+'\n')
                                # if this is BY, it might have been printed BY the person etc
                        elif prep == 'for' or prep =='For':
                                print line[0] + ' ' + prep + ' ' + ' '.join(c[0] for c in chunk.leaves())
                                # outputfile2.write(line[0] + '|' + ' '.join(c[0] for c in chunk.leaves())+'\n')
                    # print chunk.leaves()
                    #print(line[0] + '|' +' '.join(c[0] for c in chunk.leaves())+'\n')
                    # outputfile.write(line[0] + '|' +' '.join(c[0] for c in chunk.leaves())+'\n')

    inputfile.close()
    # outputfile1.close()
    # outputfile2.close()

if __name__ == "__main__":
    extract_ent()