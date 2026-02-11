#!/usr/bin/env python3

import sys

if (len(sys.argv) != 3):
    print("none")
    exit(1)

print(list(range(int(sys.argv[1]), int(sys.argv[2]) + 1)))
