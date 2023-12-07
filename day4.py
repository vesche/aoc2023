import re

with open('day4_input.txt') as f:
    data = f.read().splitlines()

class Card:
    def __init__(self, winning_numbers, numbers):
        self.winning_numbers = winning_numbers
        self.numbers = numbers
        self.copies = 1

cards = dict()
pattern = r"Card (?P<card_number>[0-9 ]*): (?P<winning_numbers>[0-9 ]*) \| (?P<numbers>[0-9 ]*)"
for line in data:
    m = re.match(pattern, line).groupdict()
    cards[int(m['card_number'])] = Card(
        set(map(int, m['winning_numbers'].split())),
        set(map(int, m['numbers'].split())),
    )

part1 = 0
for card_number, card in cards.items():
    for _ in range(card.copies):
        matches = len(card.winning_numbers & card.numbers)
        increase_copies = [card_number + 1 + n for n in range(matches)]
        for cn in increase_copies:
            cards[cn].copies += 1
    if matches:
        part1 += 2 ** (matches - 1)
print(part1)
print(sum(card.copies for card in cards.values()))

