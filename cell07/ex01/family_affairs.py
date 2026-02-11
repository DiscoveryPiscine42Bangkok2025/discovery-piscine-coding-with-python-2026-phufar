#!/usr/bin/env python3

def find_the_redheads(dict_fam):
    return list(filter(lambda x : dict_fam[x] == "red", dict_fam.keys()))

dupont_family = {
    "florian" : "red",
    "marie" : "blond",
    "virginie" : "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
