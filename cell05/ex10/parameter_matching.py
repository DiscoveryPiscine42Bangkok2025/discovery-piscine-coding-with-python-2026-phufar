#!/usr/bin/env python3

import sys

if (len(sys.argv)) != 2 :
    print("none")
    exit(1)

input_text = input("What was the paramter? ")

if (input_text == sys.argv[1]):
    print("Good job!")
else:
    print("Nope, sorry...")
