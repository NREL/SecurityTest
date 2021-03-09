import pickle
import sys
from urllib.request import urlopen

obj = pickle.loads(urlopen(sys.argv[1]).read())
print(obj)


with open('serial', 'r') as f:
    pickle.loads(f.read())


#this is a test code snippet that should trigger security problems
