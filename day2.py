import re

with open('day2_input.txt') as f:
    data = f.read().splitlines()

max_r, max_g, max_b = 12, 13, 14
pattern = r"Game (?P<game_id>[0-9]*): (?P<cube_data>.*)"

part1, part2 = 0, 0
for line in data:
    m = re.match(pattern, line).groupdict()
    cube_data = [i.split() for i in m['cube_data'].replace(';',',').split(',')]
    valid = True
    high_r, high_g, high_b = 0, 0, 0
    for n, color in cube_data:
        amount = int(n)
        if (color == 'red' and amount > max_r) or \
           (color == 'green' and amount > max_g) or \
           (color == 'blue' and amount > max_b):
            valid = False
        if color == 'red' and high_r < amount:
            high_r = amount
        if color == 'green' and high_g < amount:
            high_g = amount
        if color == 'blue' and high_b < amount:
            high_b = amount
    if valid:
        part1 += int(m['game_id'])
    part2 += (high_r * high_g * high_b)
print(part1, part2)

