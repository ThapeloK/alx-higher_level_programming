#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = 0
        prev = 0
        for c in roman_string:
            if d[c] > prev:
                n += d[c] - prev * 2
            else:
                n += d[c]
            prev = d[c]
        return n
    return 0
