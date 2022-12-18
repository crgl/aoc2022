import numpy as np
import pandas as pd
from copy import deepcopy

def parse_input():
    with open('input.txt', 'r') as f:
        trees = []
        for line in f.readlines():
            trees.append([int(t) for t in line.strip()])
    return np.asarray(trees)

def treecomp(df):
    return df.cummax().shift(1).fillna(-1)

def p1(trees):
    trees = pd.DataFrame(trees).astype(int)
    down = trees > trees.pipe(treecomp)
    right = (trees.T > trees.T.pipe(treecomp)).T
    up = (trees.iloc[::-1] > trees.iloc[::-1].pipe(treecomp)).iloc[::-1]
    left = (trees.T.iloc[::-1] > trees.T.iloc[::-1].pipe(treecomp)).iloc[::-1].T
    visible_trees = (down | up | right | left).sum().sum()
    print("P1:", visible_trees)


def p2(trees):
    trees = pd.DataFrame(trees).astype(int)
    max_score = 0
    h = trees.shape[0]
    w = trees.shape[1]
    for i in range(h):
        for j in range(w):
            ref = trees.iloc[i, j]
            l = 0
            ptr = j
            while ptr > 0:
                ptr -= 1
                l += 1
                if trees.iloc[i, ptr] >= ref:
                    break
            r = 0
            ptr = j
            while ptr + 1 < w:
                ptr += 1
                r += 1
                if trees.iloc[i, ptr] >= ref:
                    break
            u = 0
            ptr = i
            while ptr > 0:
                ptr -= 1
                u += 1
                if trees.iloc[ptr, j] >= ref:
                    break
            d = 0
            ptr = i
            while ptr + 1 < h:
                ptr += 1
                d += 1
                if trees.iloc[ptr, j] >= ref:
                    break
            score = l * r * u * d
            if score > max_score:
                max_score = score
    print("P2:", max_score)


if __name__ == '__main__':
    trees = parse_input()
    p1(trees)
    p2(trees)
