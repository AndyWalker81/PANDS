# https://www.codegrepper.com/code-examples/python/pass+a+file+as+argument+in+python+sys+argv
# find more references

import sys

filename = sys.argv[1]

with open (filename, "rt") as f:
    data = f.read()
    e = data.count("e")
    E = data.count("E")
    print ("There are {} occurances of 'e' and there are {} occurances of 'E'".format(e, E))
    print ("Therefore, there is a total of {} occurances".format(e + E ) )