#!/usr/bin/env python

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

def parse_line(line):
    ranges = []
    items = line.split(",")
    for i in items:
        nums = i.split("-")
        ranges.append((int(nums[0]), int(nums[1])))
    return ranges

def overlap(a, b):
    if a[0] >= b[0] and a[0] <= b[1]:
        return True
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    elif b[0] >= a[0] and b[0] <= a[1]:
        return True
    elif b[1] >= a[0] and b[1] <= a[1]:
        return True
    else:
        return False

total = 0
for line in data.split("\n"):
    if len(line) > 0:
        ranges = parse_line(line)
        if overlap(ranges[0], ranges[1]):
            print(f"overlap: {ranges}")
            total += 1

print(f"total: {total}")

