#!/bin/python

from pprint import pprint, pformat
import re
import math
import sys

sys.path.append('../')

from helpers import get_input

with open('./input.txt') as file:
    content = file.read().splitlines()


NORMAL_CHARACTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']


def has_number_adjacent_symbol(map: list[str], number_start: int, number_end: int, number_row: int):
    for i in range(number_start-1, number_end+1):
        try:
            if map[number_row-1][i] not in NORMAL_CHARACTERS:
                return True
            if map[number_row+1][i] not in NORMAL_CHARACTERS:
                return True
        except IndexError:
            continue
    try:
        if map[number_row][number_start-1] not in NORMAL_CHARACTERS:
            return True
    except IndexError:
        pass
    try:
        if map[number_row][number_end] not in NORMAL_CHARACTERS:
            return True
    except IndexError:
        pass
    return False


def found_gear_multiplier(map: list[str], number_start: int, number_end: int, number_row: int) -> tuple:
    for i in range(number_start-1, number_end+1):
        try:
            if map[number_row-1][i] == '*':
                return (number_row-1, i)
            if map[number_row+1][i] == '*':
                return (number_row+1, i)
        except IndexError:
            continue
    try:
        if map[number_row][number_start-1] == '*':
            return (number_row, number_start-1)
    except IndexError:
        pass
    try:
        if map[number_row][number_end] == '*':
            return (number_row, number_end)
    except IndexError:
        pass
    return

def exercise_1():
    content = get_input()
    numbers_sum = 0

    for i, row in enumerate(content):
        found_numbers = re.finditer(r'[0-9]+', row)
        for number in found_numbers:
            number_start, number_end = number.span()
            if has_number_adjacent_symbol(content, number_start, number_end, i):
                numbers_sum += int(number.group(0))
    print(numbers_sum)

def exercise_2():
    content = get_input()
    asterisk = {}

    for i, row in enumerate(content):
        found_numbers = re.finditer(r'[0-9]+', row)
        for number in found_numbers:
            number_start, number_end = number.span()
            is_asterisk = found_gear_multiplier(content, number_start, number_end, i)
            if is_asterisk:
                if asterisk.get(is_asterisk):
                    asterisk.get(is_asterisk).append(int(number.group(0)))
                else:
                    asterisk[is_asterisk] = [int(number.group(0))]

    total_sum = sum([math.prod(nums) for nums in asterisk.values() if len(nums) == 2])
    print(total_sum)


if __name__ == '__main__':
    print('Part #01:', end=" ")
    exercise_1()
    print('Part #02:', end=" ")
    exercise_2()

