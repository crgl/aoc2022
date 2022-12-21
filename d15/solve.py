import numpy as np
import pandas as pd
from copy import deepcopy
from time import time

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

def p1(sensors, beacons, manhattans):
    y = 2_000_000 # row of interest
    min_x = min((sensor[0] for sensor in sensors)) - max(manhattans)
    max_x = max((sensor[0] for sensor in sensors)) + max(manhattans)
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
    excluded = sum(r[1] - r[0] + 1 for r in new_ranges) - len([b for b in set(beacons) if b[1] == y])
    print("P1:", excluded)

def p2(sensors, manhattans):
    min_val = 0
    max_val = 4_000_000
    options = []
    for y in range(min_val, max_val + 1):
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
        if len(new_ranges) > 1:
            assert new_ranges[0][1] + 1 == new_ranges[1][0] - 1
            assert min_val <= new_ranges[0][1] + 1 <= max_val # really should be a conditional
            options.append((new_ranges[0][1] + 1, y))
        elif new_ranges[0][0] > min_val:
            assert new_ranges[0][0] == min_val + 1
            options.append((min_val, y))
        elif new_ranges[0][1] < max_val:
            assert new_ranges[0][1] + 1 == max_val
            options.append((max_val, y))
    assert len(options) == 1
    output = options[0]
    print("P2:", output[0] * max_val + output[1])

if __name__ == '__main__':
    sensors, beacons, manhattans = parse_input()
    st = time()
    p1(sensors, beacons, manhattans)
    p1_time = time() - st
    print(p1_time)
    p2(sensors, manhattans)
    p2_time = time() - st - p1_time
    print(p2_time)
