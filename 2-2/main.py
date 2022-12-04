#!/usr/bin/env python


with open("input.txt", "r") as f:
    data = f.read()
    f.close()

def score(a, b):
    a = ord(a.lower()) - 97
    b = ord(b.lower()) - 120
    if b == 0:
        # lose
        return ((a - 1) % 3) + 1
    elif b == 1:
        # draw
        return a + 4
    else:
        # win
        return ((a + 1) % 3) + 7

total = 0
for line in data.split("\n"):
    items = line.split(" ")
    if len(items) == 2:
        total += score(items[0], items[1])
        print(f"{items}: {total}")

print(f"score {total}")
