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

def drag(hpos, tpos):
    hy, hx = hpos
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
    return (hpos, tpos)

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
        hpos = (hy, hx)
        hpos, tpos = drag(hpos, tpos)
        tpos_rec.add(tpos)
    print("P1:", len(tpos_rec))


def p2(moves):
    positions = [(0, 0)] * 10
    tpos_rec = set()
    tpos_rec.add(positions[-1])
    for move in moves:
        dy, dx = move
        hy, hx = positions[0]
        hy += dy
        hx += dx
        positions[0] = (hy, hx)
        for i in range(9):
            hpos = positions[i]
            tpos = positions[i + 1]
            hpos, tpos = drag(hpos, tpos)
            positions[i] = hpos
            positions[i + 1] = tpos
        tpos_rec.add(positions[-1])
    print("P2:", len(tpos_rec))


if __name__ == '__main__':
    moves = parse_input()
    p1(moves)
    p2(moves)
