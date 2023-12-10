#!/bin/python

from pprint import pprint, pformat
import sys

sys.path.append('../')

from helpers import get_input


def parse_single_grab(game: str) -> dict:
    balls = {
        'green': 0,
        'blue': 0,
        'red': 0,
    }
    # print(f"\n {game=}")
    all_collected_balls = game.split(',')
    for collected_balls in all_collected_balls:
        count, color = collected_balls.strip().split(' ')
        balls[color] += int(count)
    return balls


def parse_all_grabs(all_grabs: list[str]) -> list[dict]:
    return [parse_single_grab(grab) for grab in all_grabs]


def parse_input_file_line(line):
    game_no = int(line.split(':')[0].split(' ')[-1])
    all_games = line.split(':')[1].split(';')
    all_games = parse_all_grabs(all_games)
    return game_no, all_games


def is_grab_possible(balls_count: dict) -> bool:
    return (0 <= balls_count['red'] <= 12) and (0 <= balls_count['green'] <= 13) and (0 <= balls_count['blue'] <= 14)


def get_power_of_game_set(balls_count_of_game: list[dict]) -> int:
    maximum_red   = max([balls.get('red')   for balls in balls_count_of_game])
    maximum_green = max([balls.get('green') for balls in balls_count_of_game])
    maximum_blue  = max([balls.get('blue')  for balls in balls_count_of_game])
    return maximum_red * maximum_blue * maximum_green


def exercise_1():
    lines = get_input()
    possible_indexes = []
    for line in lines:
        game_no, all_grabs = parse_input_file_line(line)
        are_grabs_possible = [True for game in all_grabs if is_grab_possible(game)]
        if are_grabs_possible:
            possible_indexes.append(game_no)
    print(sum(possible_indexes))


def exercise_2():
    lines = get_input()
    lets_count = 0
    for line in lines:
        _, parsed_all_games = parse_input_file_line(line)
        lets_count += get_power_of_game_set(parsed_all_games)
    print(lets_count)


if __name__ == '__main__':
    print('Part #01:', end=" ")
    exercise_1()
    print('Part #02:', end=" ")
    exercise_2()