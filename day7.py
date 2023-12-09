
with open('day7_input.txt') as f:
    data = f.read().splitlines()

def get_hand_strength(cards, part2=False):
    if part2 and "J" in cards and not list(cards.keys()) == ["J"]:
        n = cards.pop("J")
        cards[max(cards, key=cards.get)] += n

    strength = 0
    if 2 in cards.values():
        strength = 1
    if list(cards.values()).count(2) == 2:
        strength = 2
    if 3 in cards.values():
        strength = 3
    if 3 in cards.values() and 2 in cards.values():
        strength = 4
    if 4 in cards.values():
        strength = 5
    if 5 in cards.values():
        strength = 6
    return strength

hands = []
for line in data:
    hand, bid = line.split()
    cards = {card:hand.count(card) for card in set(hand)}
    strength_part1 = get_hand_strength(cards)
    strength_part2 = get_hand_strength(cards, part2=True)
    hands.append(
        {
            "hand": hand,
            "strength_part1": strength_part1,
            "strength_part2": strength_part2,
            "bid": int(bid)
        }
    )

ranking_part1 = 'AKQJT98765432'
ranking_part2 = 'AKQT98765432J'
rank_part1, rank_part2 = 1, 1
part1, part2 = 0, 0

def order_up(hands, ranking):
    return sorted(hands, key=lambda x: [ranking.index(i) for i in x["hand"]], reverse=True)

for s in range(7):
    current_hands_part1 = order_up([h for h in hands if h["strength_part1"] == s], ranking_part1)
    current_hands_part2 = order_up([h for h in hands if h["strength_part2"] == s], ranking_part2)
    for hand in current_hands_part1:
        part1 += hand["bid"] * rank_part1
        rank_part1 += 1
    for hand in current_hands_part2:
        part2 += hand["bid"] * rank_part2
        rank_part2 += 1

print(part1)
print(part2)
