#!/usr/bin/env python

from collections import defaultdict

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

def priority(c):
    if ord(c) >= 97 and ord(c) <= 122:
        # lowercase
        return ord(c) - 96
    else:
        # uppercase
        return ord(c) - 38

def process_group(lines):
    d1 = {}
    for c in lines[0]:
        d1[c] = 1
    d2 = {}
    for c in lines[1]:
        if c in d1:
            d2[c] = 1
    for c in lines[2]:
        if c in d2:
            return priority(c)

total = 0
group = []
for line in data.split("\n"):
    if len(line) > 0:
        group.append(line)
        if len(group) == 3:
            p = process_group(group)
            print(f"priority: {p}")
            total += p
            group = []

print(f"total: {total}")

