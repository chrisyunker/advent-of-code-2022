#!/usr/bin/env python

from dataclasses import dataclass, field

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

@dataclass
class Coord:
    x: int = 0
    y: int = 0

commands = []
for line in list(filter(lambda x: len(x) > 0, data.split("\n"))):
    items = line.split()
    commands.append((items[0], int(items[1])))

visited = {}
k = [Coord() for x in range(10)]

def move_tail(h, t):
    if h.x - t.x > 1:
        t.x += 1
        if h.y > t.y:
            t.y += 1
        elif h.y < t.y:
            t.y -= 1
    elif t.x - h.x > 1:
        t.x -= 1
        if h.y > t.y:
            t.y += 1
        elif h.y < t.y:
            t.y -= 1
    elif h.y - t.y > 1:
        t.y += 1
        if h.x > t.x:
            t.x += 1
        elif h.x < t.x:
            t.x -= 1
    elif t.y - h.y > 1:
        t.y -= 1
        if h.x > t.x:
            t.x += 1
        elif h.x < t.x:
            t.x -= 1
  
for command in commands:
    print(command)
    for _idx in range(command[1]):
        if command[0] == "U":
            k[0].y += 1
        elif command[0] == "D":
            k[0].y -= 1
        elif command[0] == "L":
            k[0].x -= 1
        elif command[0] == "R":
            k[0].x += 1
        else:
            print("ERROR: bad command: {command}")

        for i in range(9):
            move_tail(k[i], k[i+1])
        print(f"head: [{k[0].x}][{k[0].y}] tail: [{k[9].x}][{k[9].y}]")
        visited[(k[9].x, k[9].y)] = 1

total = len(visited)
print(f"Total visited: {total}")

