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

for c in cubes:
    m[c.x - min_x][c.y - min_y][c.z - min_z] = 1


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

