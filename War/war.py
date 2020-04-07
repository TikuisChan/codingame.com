import sys
import math

n = int(input())  # the number of cards for player 1
cardp_1 = [input() for _ in range(n)]  # the n cards of player 1
m = int(input())  # the number of cards for player 2
cardp_2 = [input() for _ in range(m)]  # the m cards of player 2
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
card_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,\
'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def single_turn(p1, p2, counter):
    if card_map[p1[counter * 4][:-1]] == card_map[p2[counter * 4][:-1]]:
        counter += 1
        if (len(p1) < 1 + counter * 4) or (len(p2) < 1 + counter * 4):
            return False
        else:
            return single_turn(p1, p2, counter)
    else:
        win = p1[0: counter * 4 + 1] + p2[0: counter * 4 + 1]
        if card_map[p1[counter * 4][:-1]] > card_map[p2[counter * 4][:-1]]:
            p1.extend(win)
        else:
            p2.extend(win)
        del(p1[0:counter * 4 + 1])
        del(p2[0:counter * 4 + 1]) 
        return True

game_round = 0
game = True

while game:
    counter = 0
    game = single_turn(cardp_1, cardp_2, counter)
    game_round += 1
    if len(cardp_2) == 0:
        print(1, game_round)
        break
    elif len(cardp_1) == 0:
        print(2, game_round)
        break
    elif not game:
        print('PAT')
    
