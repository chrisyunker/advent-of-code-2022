#!/usr/bin/env python

from collections import defaultdict
with open("input.txt", "r") as f:
    data = f.read()
    f.close()

code = data.split("\n")[0]
print(f"code: {code}")

buf = [None] * 14
d = defaultdict(int)

for idx, c in enumerate(code):
    if idx <= 13:
        buf[idx % 14] = c
        d[c] +=1 
        continue

    print(f"buffer {buf}")

    old = buf[idx % 14]
    buf[idx % 14] = c
    print(f"old: {old} new: {c}")

    if d[old] == 1:
        del d[old]
    else:
        d[old] -= 1
    d[c] +=1

    if len(d) == 14:
        print(f"first marker after character {idx+1}")
        break



