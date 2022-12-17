import numpy as np
import pandas as pd
from copy import deepcopy

def parse_input():
    with open('input.txt', 'r') as f:
        moves = []
        for line in f.readlines():
            dir, mag = line.split()
            mag = int(mag)
            if dir == 'D':
                shift = (-1, 0)
            elif dir == 'U':
                shift = (1, 0)
            elif dir == 'L':
                shift = (0, -1)
            elif dir == 'R':
                shift = (0, 1)
            else:
                print("HUH!", dir)
                exit(1)
            for _ in range(mag):
                moves.append(shift)
    return moves

def treecomp(df):
    return df.cummax().shift(1).fillna(-1)

def p1(moves):
    hpos = (0, 0)
    tpos = (0, 0)
    tpos_rec = set()
    tpos_rec.add(tpos)
    for move in moves:
        dy, dx = move
        hy, hx = hpos
        hy += dy
        hx += dx
        ty, tx = tpos
        if ty == hy:
            if hx - tx > 1:
                tx += 1
            elif hx - tx < -1:
                tx -= 1
        elif tx == hx:
            if hy - ty > 1:
                ty += 1
            elif hy - ty < -1:
                ty -= 1
        else:
            if hy - ty > 1:
                ty += 1
                if hx > tx:
                    tx += 1
                else:
                    tx -= 1
            elif hy - ty < -1:
                ty -= 1
                if hx > tx:
                    tx += 1
                else:
                    tx -= 1
            elif hx - tx > 1:
                tx += 1
                if hy > ty:
                    ty += 1
                else:
                    ty -= 1
            elif hx - tx < -1:
                tx -= 1
                if hy > ty:
                    ty += 1
                else:
                    ty -= 1
        tpos = (ty, tx)
        hpos = (hy, hx)
        tpos_rec.add(tpos)
    print("P1:", len(tpos_rec))


def p2(moves):
    print("P2:")


if __name__ == '__main__':
    moves = parse_input()
    p1(moves)
    p2(moves)
