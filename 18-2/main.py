#!/usr/bin/env python

import re
from dataclasses import dataclass, field

@dataclass
class Cor:
    x: int = 0
    y: int = 0
    z: int = 0

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

min_x = -1
max_x = -1
min_y = -1
max_y = -1
min_z = -1
max_z = -1

cubes = []
for line in list(filter(lambda x: len(x) > 0, data.split("\n"))):
    c = line.split(",")
    x = int(c[0])
    y = int(c[1])
    z = int(c[2])

    if min_x == -1 or x < min_x:
        min_x = x
    if max_x == -1 or x > max_x:
        max_x = x
    if min_y == -1 or y < min_y:
        min_y = y
    if max_y == -1 or y > max_y:
        max_y = y
    if min_z == -1 or z < min_z:
        min_z = z
    if max_z == -1 or z > max_z:
        max_z = z

    cubes.append(Cor(int(c[0]), int(c[1]), int(c[2])))

print(f"x range: {min_x} - {max_x}")
print(f"y range: {min_y} - {max_y}")
print(f"z range: {min_z} - {max_z}")
rx = max_x - min_x
ry = max_y - min_y
rz = max_z - min_z

m = [[[0 for z in range(rz + 1)]
      for y in range(ry + 1)]
     for x in range(rx + 1)]
d = [[[0 for z in range(rz + 1)]
      for y in range(ry + 1)]
     for x in range(rx + 1)]

for c in cubes:
    m[c.x - min_x][c.y - min_y][c.z - min_z] = 1
    d[c.x - min_x][c.y - min_y][c.z - min_z] = 1


num = len(cubes)
sides = num * 6
print(f"Cubes: {num}")
print(f"All sides: {sides}")

touch = 0 
for x in range(rx + 1):
    for y in range(ry + 1):
        for z in range(rz + 1):
            if m[x][y][z]:
                if x > 0 and m[x-1][y][z] == 1:
                    touch += 1
                if x < rx  and m[x+1][y][z] == 1:
                    touch += 1
                if y > 0 and m[x][y-1][z] == 1:
                    touch += 1
                if y < ry  and m[x][y+1][z] == 1:
                    touch += 1
                if z > 0 and m[x][y][z-1] == 1:
                    touch += 1
                if z < rz  and m[x][y][z+1] == 1:
                    touch += 1

print(f"Touch sides: {touch}")
sides -= touch
print(f"Exposed sides: {sides}")

def check(x, y, z):
    sides = 6
    if x == 0 or x == rx or y == 0 or y == ry or z == 0 or z == rz:
        d[x][y][z] = 2
        print(f"Hit edge: {x}, {y}, {z}")
        return (False, None)
    d[x][y][z] = 1
    if m[x-1][y][z] == 0:
        sides -= 1
        if d[x-1][y][z] == 2:
            d[x][y][z] = 2
            return (False, None)
        if d[x-1][y][z] == 0:
            res, s = check(x-1, y, z)
            if not res:
                d[x][y][z] = 2
                return (False, None)
            print(f"Add: {x-1}, {y}, {z}, sides: {s}")
            sides += s
    if m[x+1][y][z] == 0:
        sides -= 1
        if d[x+1][y][z] == 2:
            d[x][y][z] = 2
            return (False, None)
        if d[x+1][y][z] == 0:
            res, s = check(x+1, y, z)
            if not res:
                d[x][y][z] = 2
                return (False, None)
            print(f"Add: {x+1}, {y}, {z}, sides: {s}")
            sides += s
    if m[x][y-1][z] == 0:
        sides -= 1
        if d[x][y-1][z] == 2:
            d[x][y][z] = 2
            return (False, None)
        if d[x][y-1][z] == 0:
            res, s = check(x, y-1, z)
            if not res:
                d[x][y][z] = 2
                return (False, None)
            print(f"Add: {x}, {y-1}, {z}, sides: {s}")
            sides += s
    if m[x][y+1][z] == 0:
        sides -= 1
        if d[x][y+1][z] == 2:
            d[x][y][z] = 2
            return (False, None)
        if d[x][y+1][z] == 0:
            res, s = check(x, y+1, z)
            if not res:
                d[x][y][z] = 2
                return (False, None)
            print(f"Add: {x}, {y+1}, {z}, sides: {s}")
            sides += s
    if m[x][y][z-1] == 0:
        sides -= 1
        if d[x][y][z-1] == 2:
            d[x][y][z] = 2
            return (False, None)
        if d[x][y][z-1] == 0:
            res, s = check(x, y, z-1)
            if not res:
                d[x][y][z] = 2
                return (False, None)
            print(f"Add: {x}, {y}, {z-1}, sides: {s}")
            sides += s
    if m[x][y][z+1] == 0:
        sides -= 1
        if d[x][y][z+1] == 2:
            d[x][y][z] = 2
            return (False, None)
        if d[x][y][z+1] == 0:
            res, s = check(x, y, z+1)
            if not res:
                d[x][y][z] = 2
                return (False, None)
            print(f"Add: {x}, {y}, {z+1}, sides: {s}")
            sides += s
    return (True, sides)


inner = 0
for x in range(1, rx + 1):
    for y in range(1, ry + 1):
        for z in range(1, rz + 1):
            if m[x][y][z] == 0 and d[x][y][z] == 0:
                print(f"Check {x}, {y}, {z}")
                res, i = check(x, y, z)
                if res:
                    print(f"Inner area: {x}, {y}, {z}, sides: {i}")
                    inner += i

print(f"Inter sides: {inner}")
print(f"Adjusted total sides: {sides-inner}")

