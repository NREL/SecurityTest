import pickle
import sys
from urllib.request import urlopen

obj = pickle.loads(urlopen(sys.argv[1]).read())
print(obj)

#this is a test code snippet that should trigger security problems
