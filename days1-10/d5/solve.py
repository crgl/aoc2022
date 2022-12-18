import numpy as np
from copy import deepcopy

def parse_input():
    moves = []
    stack_mode = True
    with open('input.txt', 'r') as f:
        future_stacks = []
        for line in f.readlines():
            if len(line) < 3:
                stack_mode = False
                stacks = [s[::-1] for s in future_stacks[1::4]]
                for s in stacks:
                    s.pop(0)
                    while len(s) > 0 and s[-1] == ' ':
                        s.pop()
            elif stack_mode:
                while len(line) > len(future_stacks) + 1:
                    future_stacks.append([])
                for i, c in enumerate(line[:-1]):
                    future_stacks[i].append(c)
            else:
                nums = [int(n) for n in line.split()[1::2]]
                moves.append((nums[0], nums[1] - 1, nums[2] - 1))
    return (stacks, moves)

def p1(stacks, moves):
    message = ""
    for move in moves:
        for _ in range(move[0]):
            to_move = stacks[move[1]].pop()
            stacks[move[2]].append(to_move)
    for s in stacks:
        message += s.pop()
    print("P1:", message)

def p2(stacks, moves):
    message = ""
    to_move = []
    for move in moves:
        for _ in range(move[0]):
            to_move.append(stacks[move[1]].pop())
        while len(to_move) > 0:
            stacks[move[2]].append(to_move.pop())
    for s in stacks:
        message += s.pop()
    print("P2:", message)

if __name__ == '__main__':
    stacks, moves = parse_input()
    p1(deepcopy(stacks), moves)
    p2(deepcopy(stacks), moves)
