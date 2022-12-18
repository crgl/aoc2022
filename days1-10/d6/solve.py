import numpy as np
from copy import deepcopy

def parse_input():
    with open('input.txt', 'r') as f:
        return f.readline().strip()

def p1(signal):
    output = 0
    for i in range(len(signal) - 3):
        if len(set(signal[i:i+4])) == 4:
            output = i + 4
            break
    print("P1:", output)

def p2(signal):
    output = 0
    for i in range(len(signal) - 13):
        if len(set(signal[i:i+14])) == 14:
            output = i + 14
            break
    print("P2:", output)

if __name__ == '__main__':
    signal = parse_input()
    p1(signal)
    p2(signal)
