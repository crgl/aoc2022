import numpy as np
import pandas as pd
from copy import deepcopy
from time import time
from concurrent.futures import ProcessPoolExecutor

def parse_input():
    sensors = []
    beacons = []
    manhattans = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            sensor, beacon = line.strip().split(':')
            coords = sensor.split(', y=')
            sensex = int(coords[0].split('=')[1])
            sensey = int(coords[1])
            sensors.append((sensex, sensey))
            coords = beacon.split(', y=')
            beacx = int(coords[0].split('=')[1])
            beacy = int(coords[1])
            beacons.append((beacx, beacy))
            manhattans.append(abs(beacx - sensex) + abs(beacy - sensey))
    return (sensors, beacons, manhattans)

def get_covered_ranges(y, sensors, manhattans):
    ranges = []
    for sensor, dist in zip(sensors, manhattans):
        ydist = abs(sensor[1] - y)
        if ydist <= dist:
            halfrange = dist - ydist
            ranges.append((sensor[0] - halfrange, sensor[0] + halfrange))
    new_ranges = []
    ranges.sort()
    currx1, currx2 = ranges[0]
    for x1, x2 in ranges:
        if x1 <= currx2:
            currx2 = max(x2, currx2)
        else:
            new_ranges.append((currx1, currx2))
            currx1, currx2 = x1, x2
    if (currx1, currx2) not in new_ranges:
        new_ranges.append((currx1, currx2))
    return new_ranges

def p1(sensors, beacons, manhattans):
    y = 2_000_000 # row of interest
    new_ranges = get_covered_ranges(y, sensors, manhattans)
    excluded = sum(r[1] - r[0] + 1 for r in new_ranges) - len([b for b in set(beacons) if b[1] == y])
    print("P1:", excluded)

def get_coverage(yvals, min_val=0, max_val=4_000_000):
    sensors, _beacons, manhattans = parse_input()
    outputs = []
    for y in yvals:
        new_ranges = get_covered_ranges(y, sensors, manhattans)
        if len(new_ranges) > 1 and new_ranges[0][1] + 1 == new_ranges[1][0] - 1 and min_val <= new_ranges[0][1] + 1 <= max_val:
            outputs.append((new_ranges[0][1] + 1, y))
        elif new_ranges[0][0] > min_val and new_ranges[0][0] == min_val + 1:
            outputs.append((min_val, y))
        elif new_ranges[0][1] < max_val and new_ranges[0][1] + 1 == max_val:
            outputs.append((max_val, y))
    return outputs

def p2():
    min_val = 0
    max_val = 4_000_000
    diff = max_val - min_val
    lol = [range(x, x + diff // 100 + 1) for x in range(min_val, max_val, diff // 100)] # list of lists
    with ProcessPoolExecutor() as executor:
        output_sets = [val for val in executor.map(get_coverage, lol) if val != []]
    for output_set in output_sets:
        for output in output_set:
            print("P2:", output[0] * max_val + output[1])

if __name__ == '__main__':
    sensors, beacons, manhattans = parse_input()
    p1(sensors, beacons, manhattans)
    p2()
