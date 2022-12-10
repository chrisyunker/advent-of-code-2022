#!/usr/bin/env python


with open("input.txt", "r") as f:
    data = f.read()
    f.close()

def print_grid(g):
    print()
    for y in range(y_size-1, -1, -1):
        for x in range(x_size):
            print(g[x][y], end="")
        print()
    print()

lines = list(filter(lambda x: len(x) > 0, data.split("\n")))

x_size = len(lines[0])
y_size = len(lines)
m = [[0 for x in range(x_size)] for y in range(y_size)]
v = [[0 for x in range(x_size)] for y in range(y_size)]

print(f"grid size: {x_size} x {y_size}")

y = y_size-1
for line in lines:
    for x, c in enumerate(line):
        m[x][y] = int(c)
    y -= 1

print("Tree grid")
print_grid(m)

visable = {}
for y in range(0, y_size):
    h = -1 
    for x in range(0, x_size):
        if m[x][y] > h:
            h = m[x][y]
            visable[(x,y)] = 1
            v[x][y] = 1
    h = -1 
    for x in range(x_size-1, -1, -1):
        if m[x][y] > h:
            h = m[x][y]
            visable[(x,y)] = 1
            v[x][y] = 1
for x in range(0, x_size):
    h = -1 
    for y in range(0, y_size):
        if m[x][y] > h:
            h = m[x][y]
            visable[(x,y)] = 1
            v[x][y] = 1
    h = -1 
    for y in range(y_size-1, -1, -1):
        if m[x][y] > h:
            h = m[x][y]
            visable[(x,y)] = 1
            v[x][y] = 1

print("Visable grid")
print_grid(v)

print(f"Total visible: {len(visable)}")

