#!/usr/bin/env python

import re
from dataclasses import dataclass, field


with open("input.txt", "r") as f:
    data = f.read()
    f.close()

@dataclass
class Node:
    up: 'Node' = None
    dirs: list['Node'] = field(default_factory=list)
    files: list[str] = field(default_factory=list)
    level: int = 0
    name: str = ""
    size: int = 0

def print_fs(dir):
    margin = " " * dir.level * 2
    print(f"{margin}- {dir.name} (dir, size={dir.size})")

    for file in dir.files:
        print(f"  {margin}- {file[0]} (file, size={file[1]})")

    for subdir in dir.dirs:
        print_fs(subdir)

def calc_size(dir):
    size = 0
    for file in dir.files:
        size += file[1]
    for subdir in dir.dirs:
        size += calc_size(subdir)
    dir.size = size
    return dir.size

def get_sizes(dir):
    sizes = [dir.size]
    for subdir in dir.dirs:
        sizes += get_sizes(subdir)
    return sizes

root = Node(name = "/")
d = root

lines = list(filter(lambda x: len(x) > 0, data.split("\n")))
while len(lines) > 0:
    line = lines.pop(0)

    m = re.match("^\$ cd (.+)$", line)
    if m:
        dir = m.groups()[0]
        if dir == "..":
            d = d.up
        elif dir == "/":
            d = root
        else:
            n = Node(name = dir,
                     level = d.level + 1,
                     up = d)
            d.dirs.append(n)
            d = n
    elif line == "$ ls":
        while len(lines) > 0 and lines[0][0] != "$":
            item = lines.pop(0).split()
            if item[0] != 'dir':
                d.files.append((item[1], int(item[0])))

calc_size(root)
print_fs(root)

total = 70000000
free = total - root.size
req = 30000000
diff = req - free
print(f"total: {total}, used: {root.size}, free: {free}, required: {req}, diff: {diff}")

if diff < 0:
    print("No deletion necessary")
else:  
    sizes = get_sizes(root)
    sizes.sort()
    for s in sizes:
        if s >= diff:
            print(f"delete dir with size: {s}")
            break
