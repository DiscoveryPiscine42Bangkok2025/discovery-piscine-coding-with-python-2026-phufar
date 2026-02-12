#!/usr/bin/env python3
from checkmate import checkmate

def main():
    Board = """\
    R...
    .K..
    ..P.
    ....\
    """
    checkmate(Board)

if __name__ == "__main__":
    main()
