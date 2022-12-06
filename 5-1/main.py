#!/usr/bin/env python

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

stack_lines = []
move_lines = []

stacks_done = False
for line in data.split("\n"):
    if len(line) > 0:
        if stacks_done:
            move_lines.append(line)
        else:
            stack_lines.insert(0, line)
    else:
        stacks_done = True

cols = len(stack_lines.pop(0).split())
print(f"number of columns: {cols}")

stacks = [[] for i in range(cols)]

y = 0
for line in stack_lines:
    x = 0
    while len(line) > 2:
        # push item to stack
        if line[1] != " ":
            stacks[x].append(line[1])

        # remove item from line (plus space if exists)
        line = line[3:]
        if line[0:1] == " ":
            line = line[1:]

        x += 1
    y += 1

print(f"init stacks: {stacks}")

def move_stack(s, n, f, t):
    print(f"move {n} blocks from {f} to {t}")
    for _ in range(n):
        item = s[f].pop()
        s[t].append(item)

for line in move_lines:
    m = line.split()
    move_stack(stacks, int(m[1]), int(m[3])-1, int(m[5])-1)

print(f"final stacks: {stacks}")

top = ""
for s in stacks:
    top += s.pop()

print(f"top stacks: {top}")

