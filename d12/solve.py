import numpy as np
import pandas as pd
from copy import deepcopy

# pathfinding!
# Build a graph?
# BFS, could also just find the minimum distance to any given point
# I think exploring the whole space is totally fine so
# Don't worry about it

class Dq():
    def __init__(self):
        self.deque = [[]]
        self.qsize = 10
        self.n = 0
    
    def append(self, item):
        if len(self.deque[-1]) == self.qsize:
            self.deque.append([item])
        else:
            self.deque[-1].append(item)
        self.n += 1

    def extend(self, items):
        if len(self.deque[-1]) + len(items) <= self.qsize:
            self.deque[-1].extend(items)
        else:
            bp = self.qsize - len(self.deque[-1])
            finisher = items[:bp]
            items = items[bp:]
            self.deque[-1].extend(finisher)
            for i in range(0, len(items), self.qsize):
                self.deque.append(items[i:i + self.qsize])
        self.n += len(items)
    
    def pop(self):
        if self.n > 0:
            to_return = self.deque[-1].pop()
            self.n -= 1
            if self.n > 0 and len(self.deque[-1]) == 0:
                self.deque.pop()
        else:
            to_return = None
        return to_return

    def pop_front(self):
        if self.n > 0:
            to_return = self.deque[0].pop(0)
            self.n -= 1
            if self.n > 0 and len(self.deque[0]) == 0:
                self.deque.pop(0)
        else:
            to_return = None
        return to_return

    def __len__(self):
        return self.n


class Maze():
    def __init__(self, terrain, start_pos, end_pos) -> None:
        self.terrain = np.asarray(terrain)
        self.start = start_pos
        self.end = end_pos

    def solve(self):
        scores = np.ones_like(self.terrain) * self.terrain.size + 1
        curr_pos = self.start
        to_explore = Dq()
        to_explore.append((curr_pos, 0))
        explored = set([curr_pos])
        while len(to_explore) > 0:
            (y, x), curr_steps = to_explore.pop_front()
            curr_steps += 1
            height = self.terrain[y, x]
            if y > 0:
                i, j = y - 1, x
                new_height = self.terrain[i, j]
                if (i, j) not in explored and new_height - height <= 1:
                    if (i, j) == self.end:
                        return curr_steps
                    explored.add((i, j))
                    to_explore.append(((i, j), curr_steps))
            if y + 1 < self.terrain.shape[0]:
                i, j = y + 1, x
                new_height = self.terrain[i, j]
                if (i, j) not in explored and new_height - height <= 1:
                    if (i, j) == self.end:
                        return curr_steps
                    explored.add((i, j))
                    to_explore.append(((i, j), curr_steps))
            if x > 0:
                i, j = y, x - 1
                new_height = self.terrain[i, j]
                if (i, j) not in explored and new_height - height <= 1:
                    if (i, j) == self.end:
                        return curr_steps
                    explored.add((i, j))
                    to_explore.append(((i, j), curr_steps))
            if x + 1 < self.terrain.shape[1]:
                i, j = y, x + 1
                new_height = self.terrain[i, j]
                if (i, j) not in explored and new_height - height <= 1:
                    if (i, j) == self.end:
                        return curr_steps
                    explored.add((i, j))
                    to_explore.append(((i, j), curr_steps))

    def p2solve(self):
        scores = np.ones_like(self.terrain) * self.terrain.size + 1
        curr_pos = self.end
        to_explore = Dq()
        to_explore.append((curr_pos, 0))
        explored = set([curr_pos])
        while len(to_explore) > 0:
            (y, x), curr_steps = to_explore.pop_front()
            curr_steps += 1
            height = self.terrain[y, x]
            if y > 0:
                i, j = y - 1, x
                new_height = self.terrain[i, j]
                if (i, j) not in explored and height - new_height <= 1:
                    scores[i, j] = curr_steps
                    explored.add((i, j))
                    to_explore.append(((i, j), curr_steps))
            if y + 1 < self.terrain.shape[0]:
                i, j = y + 1, x
                new_height = self.terrain[i, j]
                if (i, j) not in explored and height - new_height <= 1:
                    scores[i, j] = curr_steps
                    explored.add((i, j))
                    to_explore.append(((i, j), curr_steps))
            if x > 0:
                i, j = y, x - 1
                new_height = self.terrain[i, j]
                if (i, j) not in explored and height - new_height <= 1:
                    scores[i, j] = curr_steps
                    explored.add((i, j))
                    to_explore.append(((i, j), curr_steps))
            if x + 1 < self.terrain.shape[1]:
                i, j = y, x + 1
                new_height = self.terrain[i, j]
                if (i, j) not in explored and height - new_height <= 1:
                    scores[i, j] = curr_steps
                    explored.add((i, j))
                    to_explore.append(((i, j), curr_steps))
        min_journ = self.terrain.size + 1
        for i in range(self.terrain.shape[0]):
            for j in range(self.terrain.shape[1]):
                if self.terrain[i, j] == 0:
                    if scores[i, j] < min_journ:
                        min_journ = scores[i, j]
        return min_journ

def parse_input():
    with open('input.txt', 'r') as f:
        terrain = []
        start_pos = (-1, -1)
        end_pos = (-1, -1)
        for i, line in enumerate(f.readlines()):
            lat = []
            for j, c in enumerate(line.strip()):
                if c == 'S':
                    lat.append(0)
                    start_pos = (i, j)
                elif c == 'E':
                    lat.append(25)
                    end_pos = (i, j)
                else:
                    lat.append(ord(c) - ord('a'))
            terrain.append(lat)
    return Maze(terrain, start_pos, end_pos)

def p1(maze):
    num_steps = maze.solve()
    print("P1:", num_steps)

def p2(maze):
    num_steps = maze.p2solve()
    print("P2:", num_steps)



if __name__ == '__main__':
    maze = parse_input()
    p1(deepcopy(maze))
    p2(deepcopy(maze))
