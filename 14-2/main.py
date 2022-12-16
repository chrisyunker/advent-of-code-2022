#!/usr/bin/env python

from functools import cmp_to_key
import copy

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

min_x = -1
max_x = -1
max_y = -1

lines = []
for l in list(filter(lambda x: len(x) > 0, data.split("\n"))):
    coords = []
    for c in l.split(" -> "):
        x, y = c.split(",")
        x = int(x)
        y = int(y)

        if max_x == -1 or x > max_x:
            max_x = x
        if min_x == -1 or x < min_x:
            min_x = x
        if max_y == -1 or y > max_y:
            max_y = y

        coords.append((x, y))
    for i in range(0, len(coords)-1):
        lines.append((coords[i][0], coords[i][1], coords[i+1][0], coords[i+1][1]))

max_y += 2
h = max_y

min_x = 500 - max_y
max_x = 500 + max_y
w = max_x - min_x
m = [['.' for y in range(h+1)] for x in range(w+1)]

def display_board():
    for y in range(h+1):
        print(f"{y} ".rjust(4, " "), end="")
        for x in range(w+1):
            print(f"{m[x][y]}", end="")
        print()
    print()

display_board()
print(f"x range: {min_x} - {max_x}")
print(f"y range: {0} - {max_y}")

for x in range(min_x, max_x+1):
    m[x-min_x][max_y] = '#'

for l in lines:
    print(f"line: {l}")
    if l[0] != l[2]:
        if l[0] < l[2]:
            for x in range(l[0], l[2]+1):
                m[x - min_x][l[1]] = '#'
        else:
            for x in range(l[2], l[0]+1):
                m[x - min_x][l[1]] = '#'
    else:
        if l[1] < l[3]:
            for y in range(l[1], l[3]+1):
                m[l[0] - min_x][y] = '#'
        else:
            for y in range(l[3], l[1]+1):
                m[l[0] - min_x][y] = '#'

display_board()

def drop(x, y):
    while True:
        if m[x-min_x][y] == 'o':
            print(f"Hit top: {y}")
            return False
        if y == max_y:
            print(f"Outside max y: {y}")
            return False
        elif m[x-min_x][y+1] == '.':
            y += 1
        elif x == min_x:
            print(f"Outside min x: {x}")
            return False
        elif m[x-min_x-1][y+1] == '.':
            x -= 1
            y += 1
        elif x == max_x:
            print(f"Outside max x: {x}")
            return False
        elif m[x-min_x+1][y+1] == '.':
            x += 1
            y += 1
        else:
            m[x-min_x][y] = 'o'
            return True

count = 0
while True:
    res = drop(500, 0)
    if not res:
        break
    count += 1

display_board()
print(f"Count: {count}")


