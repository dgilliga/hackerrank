#!/bin/python3

"""
    You must answer q queries, where each query i consists of a string, s_i. For each query, print YES on a new line if
    s_i contains hackerrank; otherwise, print NO instead.
"""

# !/bin/python3

import sys

hackerank_str = "hackerrank"
cur_index = 0
last_index = len(hackerank_str) - 1

q = int(input().strip())
for a0 in range(q):
    cur_index = 0
    s = input().strip()
    for l in s:
        if l == hackerank_str[cur_index]:
            cur_index += 1
            if cur_index > last_index:
                break
    if cur_index > last_index:
        print("YES")
    else:
        print("NO")
