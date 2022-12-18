import numpy as np
import pandas as pd
from copy import deepcopy


class Monkey():
    def __init__(self, notes) -> None:
        self.items = []
        self.inspections = 0
        self.throws = []
        for comps in notes:
            if comps[0] == 'Monkey':
                self.name = int(comps[1].strip(':,'))
            elif comps[0] == 'Starting':
                self.items = [int(v.strip(':,')) for v in comps[2:]]
            elif comps[0] == 'Operation:':
                if comps[-3] == 'old':
                    if comps[-1] == 'old':
                        if comps[-2] == '*':
                            self.op = lambda val: val * val
                        elif comps[-2] == '+':
                            self.op = lambda val: val + val
                        else:
                            print("HUH", comps)
                            exit(1)
                    else:
                        if comps[-2] == '*':
                            op_val = int(comps[-1])
                            self.op = lambda val: val * op_val
                        elif comps[-2] == '+':
                            op_val = int(comps[-1])
                            self.op = lambda val: val + op_val
                        else:
                            print("HUH", comps)
                            exit(1)
                elif comps[-1] == 'old':
                        if comps[-2] == '*':
                            op_val = int(comps[-3])
                            self.op = lambda val: val * op_val
                        elif comps[-2] == '+':
                            op_val = int(comps[-3])
                            self.op = lambda val: val + op_val
                        else:
                            print("HUH", comps)
                            exit(1)
                else:
                    print("HUH", comps)
                    exit(1)
            elif comps[0] == 'Test:':
                comp_val = int(comps[-1])
                self.comp_val = comp_val
                self.comp = lambda val: (val % comp_val) == 0
            elif comps[1] == 'true:':
                self.throws.append(int(comps[-1]))
            elif comps[1] == 'false:':
                self.throws.append(int(comps[-1]))
            else:
                print("HUH", comps)
                exit(1)
        self.test = lambda val: self.throws[0] if self.comp(val) else self.throws[1]

def parse_input():
    with open('input.txt', 'r') as f:
        notes = []
        monkeys = []
        for line in f.readlines():
            comps = line.split()
            if len(comps) == 0:
                monkeys.append(Monkey(notes))
                notes = []
            else:
                notes.append(comps)
        if notes != []:
            monkeys.append(Monkey(notes))
    return monkeys

def p1(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspections += len(monkey.items)
            for item in monkey.items:
                item = monkey.op(item)
                item //= 3
                target = monkey.test(item)
                monkeys[target].items.append(item)
            monkey.items = []
    inspections = sorted([monkey.inspections for monkey in monkeys])
    print("P1:", inspections[-2] * inspections[-1])

def p2(monkeys):
    modder = 1
    for comp_val in (monkey.comp_val for monkey in monkeys):
        modder *= comp_val
    for _ in range(10_000):
        for monkey in monkeys:
            monkey.inspections += len(monkey.items)
            for item in monkey.items:
                item = monkey.op(item)
                item = item % modder
                target = monkey.test(item)
                monkeys[target].items.append(item)
            monkey.items = []
    inspections = sorted([monkey.inspections for monkey in monkeys])
    print("P2:", inspections[-2] * inspections[-1])



if __name__ == '__main__':
    monkeys = parse_input()
    p1([deepcopy(monkey) for monkey in monkeys])
    p2([deepcopy(monkey) for monkey in monkeys])
