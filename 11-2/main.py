#!/usr/bin/env python

import re
from dataclasses import dataclass, field

with open("input.txt", "r") as f:
    data = f.read()
    f.close()

@dataclass
class Monkey:
    id: int = 0
    items: list[int] = field(default_factory=list)
    op: str = ""
    operand: str = ""
    div: int = 1
    true: int = 0
    false: int = 0
    inspected: int = 0

monkeys = {} 

lines = data.split("\n")
while len(lines) > 0:
    monkey = Monkey()

    line = lines.pop(0)
    m = re.match("Monkey ([0-9]+):", line)
    monkey.id = int(m.groups()[0])

    line = lines.pop(0)
    m = re.match("[ ]*Starting items: (.+)", line)
    for item in re.split("\D+", m.groups()[0]):
        monkey.items.append(int(item))
    
    line = lines.pop(0)
    m = re.match("\W*Operation: new = old ([\*\+]) (.*)", line)
    monkey.op = m.groups()[0]
    monkey.operand = m.groups()[1]
    
    line = lines.pop(0)
    m = re.match("\W*Test: divisible by ([0-9]+)", line)
    monkey.div = int(m.groups()[0])
    
    line = lines.pop(0)
    m = re.match("\W*If true: throw to monkey ([0-9]+)", line)
    monkey.true = int(m.groups()[0])
    
    line = lines.pop(0)
    m = re.match("\W*If false: throw to monkey ([0-9]+)", line)
    monkey.false = int(m.groups()[0])
    
    monkeys[monkey.id] = monkey
    print(f"Added monkey: {monkey.id}")
   
    while len(lines) > 0 and lines[0] == "":
        lines.pop(0)

num = len(monkeys)

common_div = 1
for i in range(num):
    common_div *= monkeys[i].div

def do_turn(monkeys, i):
    m = monkeys[i]
    if len(m.items) == 0:
        return
    print(f"Monkey {i}:")
    for item in m.items:
        m.inspected += 1
        print(f"  Monkey inspects an item with a worry level of {item}.")

        operand = 0
        if m.operand == "old":
            operand = item
        else:
            operand = int(m.operand)

        if m.op == "+":
            item += operand
            print(f"    Worry level increases by {operand} to {item}.")
        elif m.op == "*":
            item *= operand
            print(f"    Worry level is multiplied by {operand} to {item}.")
        else:
            print(f"Bad op: {m.op}")

        if item % m.div == 0:
            print(f"    Current worry level is divisible by {m.div}.")
            print(f"    Item with worry level {item} is thrown to monkey {m.true}.")
            monkeys[m.true].items.append(item)
        else:
            print(f"    Current worry level is not divisible by {m.div}.")
            print(f"    Item with worry level {item} is thrown to monkey {m.false}.")
            monkeys[m.false].items.append(item)
    m.items = []

round = 0
while round < 10000:
    print(f"Round {round}")
    for i in range(num):
        do_turn(monkeys, i)
    print()
    for i in range(num):
        items = ", ".join(list(map(str, monkeys[i].items)))
        print(f"Monkey {i}: {items}")
    print()
    for i in range(num):
        new_items = []
        for item in monkeys[i].items:
            item = item % common_div
            new_items.append(item)
        monkeys[i].items = new_items
    round += 1

inspected = []
for i in range(num):
    inspected.append(monkeys[i].inspected)
    print(f"Monkey {i} inspected items {monkeys[i].inspected} times.")

inspected.sort()
print(f"Top two monkeys: {inspected[num-1]} and {inspected[num-2]} for {inspected[num-1] * inspected[num-2]}")

