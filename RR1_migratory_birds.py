#!/bin/python3

"""
    A flock of  birds is flying across the continent. Each bird has a type, and the different
    types are designated by the ID numbers 1-5
    Given an array of  integers where each integer describes the type of a bird in the flock,
    find and print the type number of the most common bird.
    If two or more types of birds are equally common, choose the type with the smallest ID number.

"""

import sys

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))

bird_type_counts = [0 for i in range(5)]

for i in types:
    bird_type_counts[i - 1] += 1

my_max = max(bird_type_counts)
max_types = list()
for i in range(len(bird_type_counts)):
    if my_max == bird_type_counts[i]:
        max_types.append(i + 1)

print(min(max_types))