
with open("day9_input.txt") as f:
    data = f.read().splitlines()

def find_next_number(sequence):
    if len(set(sequence)) == 1:
        return sequence[0]
    else:
        diffs = [j-i for i,j in zip(sequence[:-1], sequence[1:])]
        return sequence[-1] + find_next_number(diffs)

part1, part2 = 0, 0
for line in data:
    seq = list(map(int, line.split()))
    part1 += find_next_number(seq)
    part2 += find_next_number(seq[::-1])
print(part1, part2)
