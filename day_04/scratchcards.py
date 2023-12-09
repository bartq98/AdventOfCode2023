#!/bin/python

from pprint import pprint, pformat
import re
import sys

sys.path.append('../')

from helpers import get_input

def parse_cards() -> list[dict]:
    unparsed_cards = get_input('./input2.txt')
    parsed_cards = []
    for unparsed_card in unparsed_cards:
        _, numbers = unparsed_card.split(':')
        winning_numbers, my_numbers = numbers.split('|')
        winning_numbers = re.findall('[0-9]+', winning_numbers)
        my_numbers = re.findall('[0-9]+', my_numbers)
        parsed_cards.append({
            'winning_numbers': set(winning_numbers),
            'my_numbers': set(my_numbers)
        })
    return parsed_cards

def exercise_1():
    cards = parse_cards()
    points = 0
    for card in cards:
        my_winning_numbers = card['winning_numbers'].intersection(card['my_numbers'])
        if my_winning_numbers:
            points += 2**(len(my_winning_numbers)-1)
    print(points)

def exercise_2():
    cards = parse_cards()
    win_scratchpads = {card_no: 1 for card_no in range(len(cards))}
    for card_no, card in enumerate(cards):
        my_winning_numbers = card['winning_numbers'].intersection(card['my_numbers'])
        for i in range(card_no+1, card_no+len(my_winning_numbers)+1):
            win_scratchpads[i] += win_scratchpads[card_no]
            """We win exactly win_scratchpads[card_no] scratchpads for next len(my_winning_numbers) cards (from current card)."""
    print(sum(win_scratchpads.values()))

if __name__ == '__main__':
    print('Part #01:', end=" ")
    exercise_1()
    print('Part #02:', end=" ")
    exercise_2()