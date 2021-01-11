#!/usr/bin/python3
"""N queens Problem"""
from sys import argv


def solve(n, i, a, b, c):
    """N queens Problem
    args:
        n - board dimension
        i - number of queens
        a, b, c - empty list
    """
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                for solution in solve(n, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    else:
        yield a

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    n = int(argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)
arr = []
for solution in solve(n, 0, [], [], []):
    for i, el in enumerate(solution):
        arr.append([i, el])
    print(arr)
    arr = []
