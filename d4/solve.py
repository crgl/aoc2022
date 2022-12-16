import numpy as np

def parse_input():
    pairs = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            pair = []
            for elf in line.strip().split(','):
                pair.append([int(sec) for sec in elf.split('-')])
            pairs.append(pair)
    return pairs

def p1(pairs):
    overlaps = 0
    for e1, e2 in pairs:
        if e1[0] > e2[0]:
            e1, e2 = e2, e1
        if e1[0] <= e2[0] and e1[1] >= e2[1]:
            overlaps += 1
        elif e1[0] == e2[0]:
            overlaps += 1
    print("P1:", overlaps)

def p2(pairs):
    overlaps = 0
    for e1, e2 in pairs:
        if e1[0] > e2[0]:
            e1, e2 = e2, e1
        if e2[0] <= e1[1]:
            overlaps += 1
    print("P2:", overlaps)

if __name__ == '__main__':
    pairs = parse_input()
    p1(pairs)
    p2(pairs)
