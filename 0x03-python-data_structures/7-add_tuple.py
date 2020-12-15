#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l = tuple_a + (0, 0)
    l1 = tuple_b + (0, 0)
    return (l[0] + l1[0], l[1] + l1[1])
