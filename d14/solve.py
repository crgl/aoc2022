import numpy as np
import pandas as pd
from copy import deepcopy
from time import time

def parse_input():
    blocks = set()
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            start_x = -1
            start_y = -1
            for comp in line.strip().split(' -> '):
                coords = [int(val) for val in comp.split(',')]
                if start_y == -1:
                    start_x = coords[0]
                    start_y = coords[1]
                    blocks.add((start_x, start_y))
                else:
                    while coords[0] < start_x:
                        start_x -= 1
                        blocks.add((start_x, start_y))
                    while coords[0] > start_x:
                        start_x += 1
                        blocks.add((start_x, start_y))
                    while coords[1] < start_y:
                        start_y -= 1
                        blocks.add((start_x, start_y))
                    while coords[1] > start_y:
                        start_y += 1
                        blocks.add((start_x, start_y))
    return blocks

def p1(blocks, max_y):
    sand_here = set()
    sand_count = 0
    source_stack = [(500, 0)]
    source_set = set(source_stack)
    while len(source_stack) > 0:
        curr_x, curr_y = source_stack[-1]
        if (curr_x, curr_y) in sand_here:
            source_stack.pop()
        else:
            while curr_y < max_y:
                down = (curr_x, curr_y + 1)
                downleft = (curr_x - 1, curr_y + 1)
                downright = (curr_x + 1, curr_y + 1)
                if (down not in blocks) and (down not in sand_here):
                    if (curr_x, curr_y) not in source_set:
                        source_set.add((curr_x, curr_y))
                        source_stack.append((curr_x, curr_y))
                    curr_y += 1
                elif (downleft not in blocks) and (downleft not in sand_here):
                    if (curr_x, curr_y) not in source_set:
                        source_set.add((curr_x, curr_y))
                        source_stack.append((curr_x, curr_y))
                    curr_x -= 1
                    curr_y += 1
                elif (downright not in blocks) and (downright not in sand_here):
                    curr_x += 1
                    curr_y += 1
                else:
                    sand_here.add((curr_x, curr_y))
                    sand_count += 1
                    break
        if curr_y >= max_y:
            break
    print("P1:", sand_count)
    return sand_here

# quadratic! or quartic, really, filling a triangle and touching every space a lot
# cubic? just too slow
# okay. So, down, then dl, then dr
# now we're filling everything, so the only reason it won't go down is if down is filled, right?
# anywhere the sand touches will be eventually filled
# but maybe we should put a source there?
# and then stop generating from that source when it is full
# then maybe we just touch every space twice
# but is this just filling a line at a time?
# kind of. well. specifically, if it went down and right, just fill the line
# if it went down and left, you need to check down and right
# and if it went down, you need to check both
# so it's silly for down and right... that's the only option, so just fill and don't generate a source
# otherwise, generate a source
# and add them to a stack
# and finish when the stack is empty

def p2(blocks, max_y):
    sand_here = set()
    sand_count = 0
    source_stack = [(500, 0)]
    source_set = set(source_stack)
    while len(source_stack) > 0:
        curr_x, curr_y = source_stack[-1]
        if (curr_x, curr_y) in sand_here:
            source_stack.pop()
        else:
            while curr_y < max_y + 1:
                down = (curr_x, curr_y + 1)
                downleft = (curr_x - 1, curr_y + 1)
                downright = (curr_x + 1, curr_y + 1)
                if (down not in blocks) and (down not in sand_here):
                    if (curr_x, curr_y) not in source_set:
                        source_set.add((curr_x, curr_y))
                        source_stack.append((curr_x, curr_y))
                    curr_y += 1
                elif (downleft not in blocks) and (downleft not in sand_here):
                    if (curr_x, curr_y) not in source_set:
                        source_set.add((curr_x, curr_y))
                        source_stack.append((curr_x, curr_y))
                    curr_x -= 1
                    curr_y += 1
                elif (downright not in blocks) and (downright not in sand_here):
                    sand_here.add((curr_x, curr_y))
                    sand_count += 1
                    curr_x += 1
                    curr_y += 1
                else:
                    sand_here.add((curr_x, curr_y))
                    sand_count += 1
                    break
            if curr_y > max_y:
                sand_here.add((curr_x, curr_y))
                sand_count += 1
    print("P2:", sand_count)
    return sand_here

if __name__ == '__main__':
    blocks = parse_input()
    max_y = max([block[1] for block in blocks])
    sand_here = p1(deepcopy(blocks), max_y)
    or_sand_here = p2(deepcopy(blocks), max_y)
