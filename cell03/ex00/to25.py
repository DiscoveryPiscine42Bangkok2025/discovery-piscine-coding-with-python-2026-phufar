#!/usr/bin/env python3

num = int(input())

if num > 25:
    print("Error")
    exit(1)

while(num <= 25):
    print(f"Inside the loop, my variable is {num}.")
    num+=1

