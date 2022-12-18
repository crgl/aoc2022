import numpy as np

def numerize(c):
    if c < 'a':
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1

def parse_input():
    sacks = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            n = len(line)
            h1 = [numerize(c) for c in line[:n // 2]]
            h2 = [numerize(c) for c in line[n // 2:]]
            sacks.append((h1, h2))
    return sacks

def p1(sacks):
    total_prio = 0
    for h1, h2 in sacks:
        shared = set(h1) & set(h2)
        assert len(shared) == 1
        for p in shared:
            total_prio += p
    print("P1:", total_prio)

def combine_halves(tup):
    return set(tup[0]) | set(tup[1])

def p2(sacks):
    total_prio = 0
    groups = zip(sacks[::3], sacks[1::3], sacks[2::3])
    for e1, e2, e3 in groups:
        r1 = combine_halves(e1)
        r2 = combine_halves(e2)
        r3 = combine_halves(e3)
        shared = r1 & r2 & r3
        assert len(shared) == 1
        for p in shared:
            total_prio += p
    print("P2:", total_prio)

if __name__ == '__main__':
    sacks = parse_input()
    p1(sacks)
    p2(sacks)
