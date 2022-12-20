import numpy as np
import pandas as pd
from copy import deepcopy
from functools import cmp_to_key

def parse_input():
    pairs = []
    with open('input.txt', 'r') as f:
        pair = []
        status = [pair]
        val = 0
        on_deck = False
        for line in f.readlines():
            if len(line.strip()) == 0:
                pairs.append(pair)
                pair = []
                status = [pair]
            else:
                for c in line.strip():
                    if c == '[':
                        status[-1].append([])
                        status.append(status[-1][-1])
                    elif c == ']':
                        if on_deck:
                            status[-1].append(val)
                            val = 0
                        on_deck = False
                        status.pop()
                    elif c in '0123456789':
                        val = val * 10 + int(c)
                        on_deck = True
                    elif c == ',':
                        if on_deck:
                            status[-1].append(val)
                            val = 0
                        on_deck = False
                    else:
                        print("HUH", c)
                        exit(1)
        if len(pair) == 2:
            pairs.append(pair)
    assert set(len(pair) for pair in pairs) == set([2])
    return pairs


def pair_comp(l1, l2):
    for i in range(len(l1)):
        item1 = l1[i]
        if i >= len(l2):
            return 1
        else:
            item2 = l2[i]
            if type(item1) == int:
                if type(item2) == int:
                    if item1 > item2:
                        return 1
                    elif item1 < item2:
                        return -1
                else:
                    comp_val = pair_comp([item1], item2)
                    if comp_val != 0:
                        return comp_val
            elif type(item2) == int:
                comp_val = pair_comp(item1, [item2])
                if comp_val != 0:
                    return comp_val
            else:
                comp_val = pair_comp(item1, item2)
                if comp_val != 0:
                    return comp_val
    if len(l2) > len(l1):
        return -1
    return 0

def p1(pairs):
    output = 0
    for i, pair in enumerate(pairs):
        if pair_comp(pair[0], pair[1]) == -1:
            output += i + 1
    print("P1:", output)

def p2(pairs):
    v1 = [[2]]
    v2 = [[6]]
    all_packets = [v1, v2]
    for pair in pairs:
        all_packets.append(pair[0])
        all_packets.append(pair[1])
    sorted_packs = sorted(all_packets, key=cmp_to_key(pair_comp))
    i1 = sorted_packs.index(v1) + 1
    i2 = sorted_packs.index(v2) + 1
    print("P2:", i1 * i2)

if __name__ == '__main__':
    pairs = parse_input()
    p1(deepcopy(pairs))
    p2(deepcopy(pairs))
