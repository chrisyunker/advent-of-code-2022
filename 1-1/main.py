#!/usr/bin/env python


with open("input.txt", "r") as f:
    data = f.read()
    f.close()

maxelf = 0
elf = 0 
for item in data.split("\n"):
    if len(item) == 0:
        print(f"elf calories: {elf}")
        if elf > maxelf:
            maxelf = elf
            print(f"new most elf calories: {maxelf}")
            elf = 0
        else:
            elf = 0
    else:
        elf += int(item)

print(f"calories: {maxelf}")
