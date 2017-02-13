import itertools
import json
from itertools import izip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

# Open JSON file
values = open('UNIV_Emprenedoria_2016.json').read()
#print values

# Adjust formatting of JSON file
values = values.replace('\n', '')    # do your cleanup here
#print values

v = values.encode('utf-8')
#print v

# Load JSON file
v = json.loads(v)
print type(v)

for i, group in enumerate(grouper(v, 2500)):
    with open('splitted/outputbatch_{}.json'.format(i), 'w') as outputfile:
        json.dump(list(group), outputfile)