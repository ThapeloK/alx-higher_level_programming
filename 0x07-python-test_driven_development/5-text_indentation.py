#!/usr/bin/python3
"""Defines a text indention function"""


def text_indentation(text):
    """Idents the given text"""
    if type(text) != str:
        raise TypeError("text must be a string")
    s = ""
    for i in text:
        if i in '.:?':
            s += i
            print(s.strip(" "), end="\n\n")
            s = ""
        else:
            s += i
    print(s.strip(" "), end="")
