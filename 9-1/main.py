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
h = Coord()
t = Coord()

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
            h.y += 1
            move_tail(h, t)
        elif command[0] == "D":
            h.y -= 1
            move_tail(h, t)
        elif command[0] == "L":
            h.x -= 1
            move_tail(h, t)
        elif command[0] == "R":
            h.x += 1
            move_tail(h, t)
        else:
            print("ERROR: bad command: {command}")
        print(f"head: [{h.x}][{h.y}] tail: [{t.x}][{t.y}]")
        visited[(t.x, t.y)] = 1

total = len(visited)
print(f"Total visited: {total}")

