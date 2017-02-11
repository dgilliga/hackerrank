#!/bin/python3

"""
    Given an array of integers, find and print the minimum absolute difference between any two elements in the array.
"""

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# your code goes here

a.sort()
my_min = abs(a[0] - a[1])
for i in range(0, len(a)-1):
    diff = abs(a[i] - a[i + 1])
    if diff < my_min:
        my_min = diff

print(my_min)
