#!/usr/bin/env python

from dataclasses import dataclass, field

@dataclass
class Coord:
    x: int = 0
    y: int = 0

def display(g):
    for y in range(len(g)-1, -1, -1):
        for x in range(len(g[0])):
            print(g[y][x], end="")
        print()
    print()

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

lines = list(filter(lambda x: len(x) > 0, data.split("\n")))
x_size = len(lines[0])
y_size = len(lines)

map = [['' for x in range(x_size)] for y in range(y_size)]
visited = {}
distance = {}

start = Coord()
end = Coord()
lines.reverse()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == 'S':
            start.x = x
            start.y = y
            map[y][x] = 'a'
        elif c == 'E':
            end.x = x
            end.y = y
            map[y][x] = 'z'
        else:
            map[y][x] = c

print(f"Start {start}")
print(f"End {end}")

display(map)

distance[(start.x, start.y)] = 0

def check_move(s, x, y):
    print(f"Check move: [{x}, {y}]")
    if x < 0 or x >= x_size:
        return (-1, Coord())
    if y < 0 or y >= y_size:
        return (-1, Coord())
    if (ord(map[y][x]) - ord(map[s.y][s.x])) > 1:
        return (-1, Coord())

    s_d = distance[(s.x, s.y)]
    n_d = s_d + 1

    if (x, y) in distance:
        if distance[(x, y)] > n_d:
            distance[(x, y)] = n_d
    else:
        distance[(x, y)] = n_d

    print(f"Good move: [{x}, {y}]")
    return (n_d, Coord(x, y))
    

def eval_node(n):
    print(f"Start node: {n}")

    if (n.x, n.y) in visited:
        print(f"Already visited: [{n.x}, {n.y}]")
        return

    visited[(n.x, n.y)] = 1

    if n == end:
        print(f"Hit end node: {n}")
        return

    next = []
    next.append(check_move(n, n.x - 1, n.y))
    next.append(check_move(n, n.x + 1, n.y))
    next.append(check_move(n, n.x, n.y - 1))
    next.append(check_move(n, n.x, n.y + 1))

    next[:] = [i for i in next if i[0] != -1]
    list(sorted(next, key = lambda x: x[0]))

    min = 0
    if len(next) > 0:
        min = next[0][0]

    for node in next:
        if node[0] == min:
            print(f"Add node: {node[1]}")
            nodes.append(node[1])

    print(f"End node: {n}")


nodes = []
nodes.append(start)
while len(nodes) > 0:
    eval_node(nodes.pop(0))

min = distance[(end.x, end.y)]
print(f"Short path: {min}")

