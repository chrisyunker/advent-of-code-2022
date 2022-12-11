#!/usr/bin/env python

from dataclasses import dataclass, field

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

commands = []

for line in list(filter(lambda x: len(x) > 0, data.split("\n"))):
    items = line.split()
    if len(items) > 1:
        commands.append((items[0], int(items[1])))
    else:
        commands.append((items[0], 0))

def draw(cycle, x, screen):
    if (cycle % 40) >= (x-1) and (cycle % 40) <= (x+1):
        screen[cycle] = 1

screen = [0 for x in range(240)]

x = 1
cycle = 0
for command in commands:
    print(command)
    if command[0] == "addx":
        draw(cycle, x, screen)
        cycle += 1
        draw(cycle, x, screen)
        x += command[1]
        cycle += 1
    else:
        draw(cycle, x, screen)
        cycle += 1
    print(f"{cycle}: {x}")

for x in range(len(screen)):
    if screen[x] == 0:
        print(".", end="")
    else:
        print("#", end="")
    if (x+1) % 40 == 0:
        print()

