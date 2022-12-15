import numpy as np

def parse_input():
    elves = [[]]
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                elves.append([])
            else:
                elves[-1].append(int(line))
    return elves

def p1(elves):
    max_cal = 0
    for elf in elves:
        cal = sum(elf)
        if cal > max_cal:
            max_cal = cal
    print("P1:", max_cal)

def p2(elves):
    cal_counts = sorted([sum(elf) for elf in elves])
    print("P2:", sum(cal_counts[-3:]))

if __name__ == '__main__':
    elves = parse_input()
    p1(elves)
    p2(elves)
