import uuid
import csv

Publisher_EEBO_File = open("/Users/Brishti/Documents/Internships/Turtle-RDF/publishedby_final.csv", "rU")
outputfile = open("/Users/Brishti/Documents/Internships/Turtle-RDF/publishedby_final_uuid.txt", "w")

for ix, line in enumerate(Publisher_EEBO_File):
    if ix > 0: # skip header
        line = line.rstrip('\r|\n')
        print line + str(uuid.uuid4())
        outputfile.write(line + str(uuid.uuid4())+'\n')