#!/bin/python

from pprint import pprint, pformat
import re
import sys

sys.path.append('../')

from helpers import get_input

def get_numbers_from_line(line: str) -> tuple[int, int, int]:
    seeds = map(lambda x: int(x), re.findall('[0-9]+', line))
    return tuple(list(seeds))

def get_seeds() -> list[int]:
    content = get_input()
    return get_numbers_from_line(content[0])

def get_mappings() -> list[tuple[int, int, int]]:
    content = get_input()
    mappings = []
    for line in content[1:]:
        if 'map:' in line:
            mappings.append([])
        elif line:
            mappings[-1].append(get_numbers_from_line(line))
    return mappings

def get_destination_from_source(source: int, mappings: list[tuple[int, int, int]]) -> int:
    for mapping in mappings:
        destination_range_start = mapping[0]
        source_start            = mapping[1]
        range_length            = mapping[2]
        source_end = source_start+range_length-1
        if source_start <= source <= source_end:
            from_range_start = source - source_start
            return destination_range_start + from_range_start
    return source

def get_location_for_seed(seed: int, mappings_collection: list[list[tuple[int, int, int]]]) -> int:
    destination = seed
    for mappings in mappings_collection:
        destination = get_destination_from_source(destination, mappings)
    return destination

def exercise_1():
    seeds = get_seeds()
    seed_location = {}
    mappings_collection = get_mappings()
    for seed in seeds:
        seed_location[seed] = get_location_for_seed(seed, mappings_collection)
    print(min(seed_location.values()))

def get_seed_by_ranges():
    seeds = get_seeds()
    seed_starts = [num for i, num in enumerate(seeds) if not i % 2]
    seed_ranges = [num for i, num in enumerate(seeds) if i % 2]
    all_seeds = []
    for start, range_lenght in zip(seed_starts, seed_ranges):
        print(len(set(range(start, start+range_lenght))))
        # all_seeds_by_range = list(set(range(start, start+range_lenght)))
        # for seed in all_seeds_by_range:
            # all_seeds.append(seed)
    return all_seeds

def exercise_2():
    seeds = get_seed_by_ranges()
    print(seeds)
    seed_location = {}
    mappings_collection = get_mappings()
    # for seed in seeds:
    #     seed_location[seed] = get_location_for_seed(seed, mappings_collection)
    # print(min(seed_location.values()))

if __name__ == '__main__':
    print('Part #01:', end=" ")
    exercise_1()
    # Current solution of part #02 is not optimal, would change to checking whole ranges instead of single seed like at part #01
    # print('Part #02:', end=" ")
    # exercise_2()