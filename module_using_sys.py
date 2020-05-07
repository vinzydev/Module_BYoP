import sys
import os

print('Command line args are')
for i in sys.argv:
    print(i)

print ('\n\n The python path is',sys.path,'\n')

print(os.getcwd())