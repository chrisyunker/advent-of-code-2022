#!/usr/bin/env python


with open("input.txt", "r") as f:
    data = f.read()
    f.close()

def score(a, b):
    a = ord(a.lower()) - 97
    b = ord(b.lower()) - 120
    res = (b - a) % 3
    if res == 0:
        return b + 1 + 3
    elif res == 1:
        return b + 1 + 6
    else:
        return b + 1

total = 0
for line in data.split("\n"):
    items = line.split(" ")
    if len(items) == 2:
        total += score(items[0], items[1])
        print(f"{items}: {total}")

print(f"score {total}")
