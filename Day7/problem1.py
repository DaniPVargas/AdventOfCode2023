def classify_hands(manos):
    types = ["five", "poker", "full", "trio", "doble_pareja", "pareja", "value"]
    hands_dict = {t:[] for t in types}
    for mano in manos:
        tipo = obtain_hand_type(mano)
        hands_dict[tipo].append(mano)
    return hands_dict

def obtain_hand_type(mano):
    elements = set(mano)
    card_types = len(elements)
    if card_types == 5:
        if 'J' in elements:
            return "pareja"
        else:
            return "value"
    if card_types == 4:
        if 'J' in elements:
            return "trio"
        else:
            return "pareja"
    if card_types == 1:
        return "five"
    if card_types == 2:
        if 'J' in elements:
            return "five"
        else:
            if mano.count(list(elements)[0]) == 1 or mano.count(list(elements)[0]) == 4:
                return "poker"
            else:
                return "full"
    if card_types == 3:
        if 'J' in elements:
            for el in elements:
                if mano.count(el) == 3:
                    return "poker"
            if mano.count('J') == 2:
                return "poker"
            else:
                return "full"
        else:
            for el in elements:
                if mano.count(el) == 3:
                    return "trio"
            return "doble_pareja"

def order_hands(hands_dict):
    types = ["value", "pareja", "doble_pareja", "trio", "full", "poker", "five"]
    ordered_hands = []
    for t in types:
        hands = hands_dict[t]
        sorted_hands = sorted(hands, key=order_criteria, reverse=True)
        ordered_hands += sorted_hands
    return ordered_hands
        

def order_criteria(s):
    order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    return [order.index(c) for c in s]


with open("input.txt", 'r') as fp:
    lines = fp.readlines()

apuestas = {line.split()[0]:line.split()[1] for line in lines}
manos = list(apuestas.keys())

hands_dict = classify_hands(manos)
ordered_hands = order_hands(hands_dict)
premios = [int(apuestas[h]) * (i + 1) for i, h in enumerate(ordered_hands)]

print(sum(premios))