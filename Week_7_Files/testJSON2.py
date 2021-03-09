# JSON lab test 2
# Author: Andy Walker

import json
filename = "testdict.json"

def readDict():
    # this will be error if file does not exist
    # it should really just return an empty dict
    # we can do this later
    with open (filename) as f:
        return json.load(f)

somedict = readDict()
print (somedict)