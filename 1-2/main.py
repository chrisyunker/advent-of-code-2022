#!/usr/bin/env python

import heapq

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

maxelfs = [0, 0, 0]
elf = 0 
for item in data.split("\n"):
    if len(item) == 0:
        print(f"elf calories: {elf}")
        heapq.heappushpop(maxelfs, elf)
        elf = 0
    else:
        elf += int(item)

total = 0
for elf in maxelfs:
    total += elf

print(f"calories: {total}")
