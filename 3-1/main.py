#!/usr/bin/env python

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

def process_rucksack(line):
    l1, l2 = line[:len(line)//2], line[len(line)//2:]
    d1 = {}
    for c in l1:
        d1[c] = 1
    for c in l2:
        if c in d1:
            return priority(c)

total = 0
for line in data.split("\n"):
    if len(line) > 0:
        p = process_rucksack(line)
        print(f"priority: {p}")
        total += p

print(f"total: {total}")

