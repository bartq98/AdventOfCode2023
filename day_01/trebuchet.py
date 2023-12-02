#!/bin/python

# PT 1.:

def calculate_sum_of_first_and_last(file_path) -> int:
    f = open(file_path, "r")
    lines = f.readlines()

    sum = 0
    for line in lines:
        digits = [int(digit) for digit in line if digit.isnumeric()]
        first_digit = digits[0]
        last_digit  = digits[-1]
        sum += first_digit * 10 + last_digit
    return sum


# PT 2.:

def calculate_sum_of_first_and_last_with_spelled(file_path) -> int:

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

    f = open(file_path, "r")
    lines = f.readlines()

    sum = 0
    for line in lines:
        found_digits = [(i, digit) for i, _ in enumerate(line) for digit in DIGITS if line[i:i+len(digit)] == digit]
        all_digits = sorted(found_digits, key = lambda x: x[0])
        first_digit = DIGITS.get(all_digits[0][1])
        last_digit = DIGITS.get(all_digits[-1][1])
        sum += first_digit*10 + last_digit
    return sum

if __name__ == '__main__':
    first_exercise = calculate_sum_of_first_and_last('exercise_1.txt')
    print(f'First exercise: {first_exercise}')
    second_exercise = calculate_sum_of_first_and_last_with_spelled('exercise_2.txt')
    print(f'Second exercise: {second_exercise}')