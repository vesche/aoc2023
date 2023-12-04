import re

with open("day1_input.txt") as f:
    data = f.read().splitlines()

part1 = 0
for line in data:
    numbers = [i for i in line if i.isdecimal()]
    part1 += int(numbers[0] + numbers[-1])
print(part1)

part2 = 0
digits = ["-", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in data:
    yolo = {}
    for i, c in enumerate(line):
        if c.isdigit():
            yolo[i] = int(c)
    for d in digits:
        x = [m.start() for m in re.finditer(d, line)]
        for n in x:
            yolo[n] = digits.index(d)
    yolo_values = list(map(str, list(dict(sorted(yolo.items())).values())))
    part2 += int(yolo_values[0] + yolo_values[-1])
print(part2)

