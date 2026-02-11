#!/usr/bin/env python3
import sys

if(len(sys.argv) > 1):
    print("none")
    exit(1)

count = 0
while(count <= 10):
    place_string = f"Table de {count}:"
    mult = ""
    inner_count = 0
    while(inner_count <= 10):
        mult += f" {inner_count * count}"
        inner_count += 1
    print(f"{place_string}{mult}")
    count += 1
