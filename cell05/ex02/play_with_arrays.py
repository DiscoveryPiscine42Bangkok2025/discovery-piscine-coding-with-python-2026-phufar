#!/usr/bin/env python3

org_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []

for i in org_arr:
    if i > 5:
        new_arr.append(i + 2)

print(f"{org_arr}")
print(f"{new_arr}")
