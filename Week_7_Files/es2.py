# es.py
# A program to read a text file and count the number of letter e's that it contains
# Author Andy Walker

# reference: https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string
# instructions not clear on whether should return 'e' or 'E' or both


filename = "es.txt"

with open (filename, "rt") as f:
    data = f.read()
    e = data.count("e")
    E = data.count("E")
    print ("There are {} occurances of 'e' and there are {} occurances of 'E'".format(e, E))
    print ("Therefore, there is a total of {} occurances".format(e + E ) )