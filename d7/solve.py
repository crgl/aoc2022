import numpy as np
from copy import deepcopy

# Assume since there is no `pwd` that we start in the root
# (We also know this won't matter since I can see the input, but in a nod to generality)

def parse_input():
    curr_dir = ['/']
    dir_files = {}
    sizes = {}
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            comps = line.split()
            for i in range(len(curr_dir)):
                dir = '/'.join(curr_dir[:i + 1])
                if dir not in dir_files.keys():
                    dir_files[dir] = set()
            if comps[0] == '$':
                command = comps[1]
                if command == 'cd':
                    if comps[2] == '..':
                        curr_dir.pop()
                    elif comps[2] == '/':
                        curr_dir = ['/']
                    else:
                        curr_dir.append(comps[2])
            else:
                if comps[0] != 'dir':
                    fsize = int(comps[0])
                    fname = comps[1]
                    sizes['/'.join(curr_dir) + '/' + fname] = fsize
                    for i in range(len(curr_dir)):
                        dir = '/'.join(curr_dir[:i + 1])
                        dir_files[dir].add('/'.join(curr_dir) + '/' + fname)
                else:
                    if comps[1] not in dir_files.keys():
                        dir_files['/'.join(curr_dir) + '/' + comps[1]] = set()
    return (dir_files, sizes)

def p1(dir_files, sizes):
    total_size = 0
    size_threshold = 100_000
    for _dir, files in dir_files.items():
        dir_size = 0
        for f in files:
            dir_size += sizes[f]
        if dir_size <= size_threshold:
            total_size += dir_size
    print("P1:", total_size)


def p2(dir_files, sizes):
    fsystem_size = 70_000_000
    dir_sizes = []
    for dir, files in dir_files.items():
        dir_size = 0
        for f in files:
            dir_size += sizes[f]
        dir_sizes.append((dir_size, dir))
    dir_sizes.sort()
    assert(dir_sizes[-1][1] == '/')
    free_space = fsystem_size - dir_sizes[-1][0]
    needed_space = 30_000_000
    to_free = needed_space - free_space
    to_delete = 'NOT FOUND'
    for size, dir_name in dir_sizes:
        if size >= to_free:
            to_delete = size
            break
    print("P2:", to_delete)

if __name__ == '__main__':
    dir_files, sizes = parse_input()
    p1(dir_files, sizes)
    p2(dir_files, sizes)
