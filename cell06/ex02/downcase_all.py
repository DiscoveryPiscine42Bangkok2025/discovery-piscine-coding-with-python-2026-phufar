#!/usr/bin/env python3

import sys

def downcase_it(word):
   return word.lower() 

if (len(sys.argv) < 2):
    print("none")
else:
    for i in range(1, len(sys.argv)):
        print(downcase_it(sys.argv[i]))

