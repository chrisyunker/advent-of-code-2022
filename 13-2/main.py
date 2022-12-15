#!/usr/bin/env python

from functools import cmp_to_key
import copy

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

def parse(line):
    line = line[1:]
    lst = []
    n = ""
    while line[0] != ']':
        if line[0] == '[':
            (l, line) = parse(line)
            lst.append(l)
        elif line [0] == ',':
            line = line[1:]
            if len(n) > 0:
                lst.append(int(n))
                n = ""
        else:
            c, line = line[:1], line[1:]
            n += c
    if len(n) > 0:
        lst.append(int(n))
        n = ""
    line = line[1:]
    return (lst, line)

def compare_wrapper(left, right):
    return compare(copy.deepcopy(left), copy.deepcopy(right))

def compare(left, right, level=0):
    m = " " * level * 2
    print(f"{m}- Compare {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            print(f"{m}  - Right side is smaller, so inputs are NOT in the right order")
            return 1
        elif left < right:
            print(f"{m}  - Left side is smaller, so inputs are in the right order")
            return -1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        while len(left) > 0 and len(right) > 0:
            l = left.pop(0)
            r = right.pop(0)
            res = compare(l, r, level+1)
            if res == -1:
                return -1
            elif res == 1:
                return 1
            else:
                continue
        if len(left) > 0 and len(right) == 0:
            print(f"{m}  - Right side ran out of items, so inputs are NOT in the right order")
            return 1
        elif len(right) > 0 and len(left) == 0:
            print(f"{m}  - Left side ran out of items, so inputs are in the right order")
            return -1
        else:
            return 0
    else:
        if isinstance(left, int):
            left = [left]
            print(f"{m}  - Mixed types; convert left to [{left}] and retry comparison")
        elif isinstance(right, int):
            right = [right]
            print(f"{m}  - Mixed types; convert right to [{right}] and retry comparison")
        return compare(left, right, level+1)

packets = []
lines = list(filter(lambda x: len(x) > 0, data.split("\n")))
while len(lines) > 0:
    (item, _) = parse(lines.pop(0))
    packets.append(item)
packets.append(parse("[[2]]")[0])
packets.append(parse("[[6]]")[0])

new_packets = sorted(packets, key=cmp_to_key(compare_wrapper))
for i, p in enumerate(new_packets):
    print(f"{i+1} {p}")
    if p == [[2]]:
        i1 = i+1
    elif p == [[6]]:
        i2 = i+1

print(f"Key {i1} * {i2} = {i1 * i2}")

