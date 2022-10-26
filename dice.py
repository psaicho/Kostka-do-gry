import re
import operator
import random


def sum_of_random_moves(type_of_dice: int, move: int) -> int:
    return sum(random.randint(1, type_of_dice + 1) for i in range(move))


def check_text(text:str) -> bool:
    try:
        text.split()
        return True
    except (AttributeError, TypeError):
        return False


def roll_the_dice(text: str) -> list:
    patern = r"[0-9]*[D](3|4|6|8|10|12|20|100){1}((\+|\-)?[0-9]*)?"
    if check_text(text) == False or re.fullmatch(patern, text) is None:
        result = "The specified string is not code for roll of dice"
    else:
        dice = re.split("[D | \+ | \-]", text)
        if dice[0] == '':
            dice[0] = 1
        dice = list(map(int, dice))
        if len(dice) == 2:
            result = sum_of_random_moves(dice[1], dice[0])
        else:
            operators = {
                '+': operator.add,
                '-': operator.sub
            }
            opr = re.findall("[\+ | \-]", text)[0]
            result = operators.get(opr)(sum_of_random_moves(dice[1], dice[0]), dice[2])

    return result


if __name__ == "__main__":
    print(roll_the_dice("D6"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))
    print(roll_the_dice(1))
