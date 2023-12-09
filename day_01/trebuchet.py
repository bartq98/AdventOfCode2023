#!/bin/python

from pprint import pprint, pformat
import sys

sys.path.append('../')

from helpers import get_input

def exercise_1():
    lines = get_input()

    sum = 0
    for line in lines:
        digits = [int(digit) for digit in line if digit.isnumeric()]
        first_digit = digits[0]
        last_digit  = digits[-1]
        sum += first_digit * 10 + last_digit
    print(sum)

def exercise_2():
    lines = get_input()

    DIGITS = {
        'one' : 1,
        'two' : 2,
        'three': 3,
        'four' : 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
    }

    sum = 0
    for line in lines:
        found_digits = [(i, digit) for i, _ in enumerate(line) for digit in DIGITS if line[i:i+len(digit)] == digit]
        all_digits = sorted(found_digits, key = lambda x: x[0])
        first_digit = DIGITS.get(all_digits[0][1])
        last_digit = DIGITS.get(all_digits[-1][1])
        sum += first_digit*10 + last_digit
    print(sum)

if __name__ == '__main__':
    print('Part #01:', end=" ")
    exercise_1()
    print('Part #02:', end=" ")
    exercise_2()