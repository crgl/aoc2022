import numpy as np
import pandas as pd
from copy import deepcopy

def parse_input():
    with open('input.txt', 'r') as f:
        reg_vals = []
        curr_val = 1
        for line in f.readlines():
            comps = line.split()
            if comps[0] == 'noop':
                reg_vals.append(curr_val)
            elif comps[0] == 'addx':
                for _ in range(2):
                    reg_vals.append(curr_val)
                curr_val += int(comps[1])
            else:
                print("HUH", comps)
                exit(1)
    return reg_vals

def p1(reg_vals):
    cycles = [20, 60, 100, 140, 180, 220]
    total_score = 0
    for cycle in cycles:
        total_score += cycle * reg_vals[cycle - 1]
    print("P1:", total_score)


def p2(reg_vals):
    print("P2:")
    for i in range(6):
        to_draw = []
        for j in range(40):
            if abs(reg_vals[i * 40 + j] - j) <= 1:
                to_draw.append('#')
            else:
                to_draw.append('.')
        print(''.join(to_draw))



if __name__ == '__main__':
    reg_vals = parse_input()
    p1(reg_vals)
    p2(reg_vals)
