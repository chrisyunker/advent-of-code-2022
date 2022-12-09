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

def calc_del(dir, max):
    size = 0
    if dir.size <= max:
        size += dir.size
    for subdir in dir.dirs:
        size += calc_del(subdir, max)
    return size

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

max = 100000
calc_size(root)
print_fs(root)
total = calc_del(root, max)

print(f"sum of dirs less than {max}: {total}")

