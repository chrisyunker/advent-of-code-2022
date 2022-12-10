#!/usr/bin/env python

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

def print_grid(g, name):
    print()
    print(f"{name}----")
    for y in range(y_size-1, -1, -1):
        for x in range(x_size):
            print(f"[{g[x][y]}]", end="")
        print()
    print()

lines = list(filter(lambda x: len(x) > 0, data.split("\n")))

x_size = len(lines[0])
y_size = len(lines)
m = [[0 for y in range(y_size)] for x in range(x_size)]
v = [[0 for y in range(y_size)] for x in range(x_size)]

print(f"grid size: {x_size} x {y_size}")

y = y_size-1
for line in lines:
    for x, c in enumerate(line):
        m[x][y] = int(c)
    y -= 1

print_grid(m, "Tree grid")

up = [[0 for y in range(y_size)] for x in range(x_size)]
dn = [[0 for y in range(y_size)] for x in range(x_size)]
lf = [[0 for y in range(y_size)] for x in range(x_size)]
ri = [[0 for y in range(y_size)] for x in range(x_size)]

for x in range(0, x_size):
    for y in range(0, y_size):
        h = m[x][y]
        l = 0
        for z in range(y+1, y_size):
            l += 1
            if m[x][z] >= h or z == y_size-1:
                up[x][y] = l
                break
    for y in range(y_size-1, -1, -1):
        h = m[x][y]
        l = 0
        for z in range(y-1, -1, -1):
            l += 1
            if m[x][z] >= h or z == 0:
                dn[x][y] = l
                break
for y in range(0, y_size):
    for x in range(0, x_size):
        h = m[x][y]
        l = 0
        for z in range(x+1, x_size):
            l += 1
            if m[z][y] >= h or z == x_size-1:
                ri[x][y] = l
                break
    for x in range(x_size-1, -1, -1):
        h = m[x][y]
        l = 0
        for z in range(x-1, -1, -1):
            l += 1
            if m[z][y] >= h or z == 0:
                lf[x][y] = l
                break


#print_grid(up, "Up")
#print_grid(dn, "Down")
#print_grid(lf, "Left")
#print_grid(ri, "Right")

high = 0
to = [[0 for y in range(y_size)] for x in range(x_size)]
for x in range(0, x_size):
    for y in range(0, y_size):
        to[x][y] = up[x][y] * dn[x][y] * lf[x][y] * ri[x][y]
        if to[x][y] > high:
            high = to[x][y]

print_grid(to, "Total")
print(f"High score: {high}")

