#!/usr/bin/env python3

def array_of_names(dict_name):
    full_name_arr = []

    for name, last_name in dict_name.items():
        full_name = f"{name.capitalize()} {last_name.capitalize()}"
        full_name_arr.append(full_name)

    return full_name_arr

persons = {
    "jean" : "valjean",
    "grace" : "hopper",
    "xavier" : "niel",
    "fifi" : "brindacier"
}

print(array_of_names(persons))
