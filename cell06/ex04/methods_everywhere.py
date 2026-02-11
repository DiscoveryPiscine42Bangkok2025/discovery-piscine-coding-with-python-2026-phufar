#!/usr/bin/env python3

import sys

def shrink(word):
    print(f"{word[0:8]}")

def enlarge(word):
    while(len(word) <= 8):
        word += 'Z'
    print(f"{word}")

if(len(sys.argv) < 2):
    print("none")
else:
    for i in range(1,len(sys.argv)):
        if (len(sys.argv[i]) < 8):
            enlarge(sys.argv[i])
        else:
            shrink(sys.argv[i])
