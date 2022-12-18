import numpy as np

def parse_input():
    matches = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            them, you = line.split()
            matches.append((ord(them) - ord('A'), ord(you) - ord('X')))
    return matches

def p1(matches):
    total_score = 0
    for them, you in matches:
        if you == (them + 1) % 3:
            total_score += 6
        elif you == them:
            total_score += 3
        else:
            pass
        total_score += you + 1
    print("P1:", total_score)

def p2(matches):
    total_score = 0
    for them, goal in matches:
        you = (them + 2 + goal) % 3
        if you == (them + 1) % 3:
            total_score += 6
        elif you == them:
            total_score += 3
        else:
            pass
        total_score += you + 1
    print("P2:", total_score)

if __name__ == '__main__':
    matches = parse_input()
    p1(matches)
    p2(matches)
