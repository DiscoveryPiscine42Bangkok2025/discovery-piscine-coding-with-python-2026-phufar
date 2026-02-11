#!/usr/bin/env python3

def greetings(name="noble strange"):
    if type(name) != str:
        print("Error! It was not a name.")
        return

    print(f"Hello, {name}.")

greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)
