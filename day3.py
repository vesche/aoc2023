from collections import defaultdict

with open('day3_input.txt') as f:
    data = ['.'+line+'.' for line in f.read().splitlines()]

deltas = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0), (0,  0), (1,  0),
    (-1,  1), (0,  1), (1,  1), ]

def check_for_adj_symbol(x, y):
    star_x, star_y = None, None
    for delta_x, delta_y in deltas:
        try:
            new_x, new_y = x + delta_x, y + delta_y
            symbol = data[new_y][new_x]
            if symbol == '*':
                star_x, star_y = new_x, new_y
            if symbol not in '.0123456789':
                return True, star_x, star_y
        except: pass
    return False, star_x, star_y

part1 = 0
star_data = defaultdict(list)
for y, line in enumerate(data):
    holder = ''
    has_adj = False
    stars = []
    for x, c in enumerate(line):
        if c.isdigit():
            holder += c
            if not has_adj:
                has_adj, star_x, star_y = check_for_adj_symbol(x, y)
                if star_x:
                    stars.append((star_x, star_y))
        else:
            if has_adj:
                part1 += int(holder)
                if stars:
                    for star_x, star_y in stars:
                        star_data[(star_x, star_y)].append(int(holder))
            holder = ''
            has_adj = False
            stars = []
print(part1)

part2 = 0
for numbers in star_data.values():
    if len(numbers) == 2:
        part2 += numbers[0] * numbers[1]
print(part2)

