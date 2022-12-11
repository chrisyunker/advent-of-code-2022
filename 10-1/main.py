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

def boost(c, x):
    if (c+1-20) % 40 == 0:
        x *= (c+1)
        print(f"boost: {c+1} value: {x}")
        return x
    else:
        return 0

x = 1
cycle = 0
signal_sum = 0
for command in commands:
    print(command)
    if command[0] == "addx":
        cycle += 1
        signal_sum += boost(cycle, x)
        x += command[1]
        cycle += 1
        signal_sum += boost(cycle, x)
    else:
        cycle += 1
        signal_sum += boost(cycle, x)
    print(f"{cycle}: {x}")

print(f"sum of signal strengths: {signal_sum}")

