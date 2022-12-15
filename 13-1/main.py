#!/usr/bin/env python

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

def compare(left, right, level=0):
    m = " " * level * 2
    print(f"{m}- Compare {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            print(f"{m}  - Right side is smaller, so inputs are NOT in the right order")
            return 0
        elif left < right:
            print(f"{m}  - Left side is smaller, so inputs are in the right order")
            return 2
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        while len(left) > 0 and len(right) > 0:
            l = left.pop(0)
            r = right.pop(0)
            res = compare(l, r, level+1)
            if res == 0:
                return 0
            elif res == 2:
                return 2
            else:
                continue
        if len(left) > 0 and len(right) == 0:
            print(f"{m}  - Right side ran out of items, so inputs are NOT in the right order")
            return 0
        elif len(right) > 0 and len(left) == 0:
            print(f"{m}  - Left side ran out of items, so inputs are in the right order")
            return 2
        else:
            return 1
    else:
        if isinstance(left, int):
            left = [left]
            print(f"{m}  - Mixed types; convert left to [{left}] and retry comparison")
        elif isinstance(right, int):
            right = [right]
            print(f"{m}  - Mixed types; convert right to [{right}] and retry comparison")
        return compare(left, right, level+1)

pairs = []
lines = list(filter(lambda x: len(x) > 0, data.split("\n")))
while len(lines) > 0:
    (left, _) = parse(lines.pop(0))
    (right, _) = parse(lines.pop(0))
    pairs.append((left, right))

order = []
for i, p in enumerate(pairs):
    print(f"== Pair {i+1} ==")
    result = compare(p[0], p[1])
    if result == 2:
        order.append(i+1)
    print(f"Result: {result == 2}")
    print()

print(f"Pairs in the right order: {order}")
print(f"Total: {sum(order)}")
