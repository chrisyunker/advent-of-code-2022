#!/usr/bin/env python

from collections import defaultdict
with open("input.txt", "r") as f:
    data = f.read()
    f.close()

code = data.split("\n")[0]
print(f"code: {code}")

buf = [None] * 4
d = defaultdict(int)

for idx, c in enumerate(code):
    if idx <= 3:
        buf[idx % 4] = c
        d[c] +=1 
        continue

    print(f"buffer {buf}")

    old = buf[idx % 4]
    buf[idx % 4] = c
    print(f"old: {old} new: {c}")

    if d[old] == 1:
        del d[old]
    else:
        d[old] -= 1
    d[c] +=1

    if len(d) == 4:
        print(f"first marker after character {idx+1}")
        break



