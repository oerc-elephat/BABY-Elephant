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
            print "The preposition is:", i, chunks[i][0]
            return (i, chunks[i][0])
 
    return (None,None)

def verbBeforePrep(chunks, ix):
    for i in range(ix-2, -2, -2):    
        #workaround for NLTK not recognizing "printed" as a verb
        if len(chunks[i]) == 2 and (
            chunks[i][0] == 'sold' or
            chunks[i][0] == 'Sold' or
            chunks[i][0] == 'printed' or
            chunks[i][0] == 'Printed'
        ):
            print "The verb is:", chunks[i][0]
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
            print sent
            chunks = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)))
            for ix, chunk in enumerate(chunks):
                # print "chunk: ", chunk, ", index: ", ix
                if hasattr(chunk, 'label') and chunk.label() == "PERSON":
                    print "I have found a person chunk: ", chunk.leaves()
                    (prepix, prep) = prepositionBeforePerson(chunks, ix) #look back, hunting for prepositions
                    if prep:
                        verb = verbBeforePrep(chunks, prepix)
                            # if this is FOR, you know it was printed FOR the person
                        if verb:
                            print "Found verb stuff: {0} {1} {2}".format(verb, prep, chunk.leaves())
                          #  if verb == 'sold' and prep == 'by':
                          #      print line[0] + ' ' + verb + ' ' + prep + ' ' + ' '.join(c[0] for c in chunk.leaves())
                          #  elif prep == 'by' or prep =='By':
                          #      print line[0] + ' ' + prep + ' ' + ' '.join(c[0] for c in chunk.leaves())
                            # outputfile1.write(line[0] + '|' + ' '.join(c[0] for c in chunk.leaves())+'\n')
                                # if this is BY, it might have been printed BY the person etc
                          #  elif prep == 'for' or prep =='For':
                          #      print line[0] + ' ' + prep + ' ' + ' '.join(c[0] for c in chunk.leaves())
                                # outputfile2.write(line[0] + '|' + ' '.join(c[0] for c in chunk.leaves())+'\n')
                                
                                # if verb:
#                                     if verb == 'sold' and prep == 'by':
#                                         print line[0] + ' ' + verb + ' ' + prep + ' ' + ' '.join(c[0] for c in chunk.leaves())
                    # print chunk.leaves()
                    #print(line[0] + '|' +' '.join(c[0] for c in chunk.leaves())+'\n')
                    # outputfile.write(line[0] + '|' +' '.join(c[0] for c in chunk.leaves())+'\n')

    inputfile.close()
    # outputfile1.close()
    # outputfile2.close()

if __name__ == "__main__":
    extract_ent()