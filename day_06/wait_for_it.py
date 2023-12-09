#!/bin/python

from pprint import pprint, pformat
import re
import math
import sys

sys.path.append('../')

from helpers import get_input


def parse_input():
    content = get_input()
    times = map(lambda x: int(x), re.findall('[0-9]+', content[0].removeprefix('Time:').strip()))
    distances = map(lambda x: int(x), re.findall('[0-9]+', content[1].removeprefix('Distance:').strip()))
    return list(times), list(distances)

def how_many_ways_to_beat_the_record(time, record_distance):
    count_possible_records = 0
    for speed in range(time):
        remianing_time = time - speed
        distance = speed * remianing_time
        count_possible_records += (distance > record_distance) or 0
    return count_possible_records


def exercise_1():
    times, distances = parse_input()
    times_win = []
    for race in range(len(times)):
        times_win.append(how_many_ways_to_beat_the_record(times[race], distances[race]))
    print(math.prod(times_win))


def exercise_2():
    times, distances = parse_input()
    time = int(''.join(str(time) for time in times))
    distance = int(''.join(str(distance) for distance in distances))
    print(how_many_ways_to_beat_the_record(time, distance))

if __name__ == '__main__':
    parse_input()
    print('Part #01:', end=" ")
    exercise_1()
    print('Part #02:', end=" ")
    exercise_2()