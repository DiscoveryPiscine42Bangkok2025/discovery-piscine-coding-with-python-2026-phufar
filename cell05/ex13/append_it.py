#!/usr/bin/env python3

import sys

if(len(sys.argv) < 2):
    print("none")
    exit(1)

for value in sys.argv[1:]:
    if not value.endswith("ism"):
        print(f"{value}ism")
