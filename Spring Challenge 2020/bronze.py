import sys
import math
import random

def pel_dis(pacX, pacY, x, y):
    return abs(pacX - x) + abs(pacY - y)

def dission(pacX, pacY, big_pel, small_pel):
    dis_min = 1000
    pell = big_pel if len(big_pel) >= 1 else small_pel
    for (x, y), dis in pell.items():
        if dis < dis_min:
            targetX, targetY = x, y
            dis_min = dis
    return targetX, targetY

def stuck(pacX, pacY, allPac):
    for pac, [x, y, big, small, side] in allPac.items():
        if x == pacX + 1:
            return 0, pacY
        elif x == pacX - 1:
            return width - 1, pacY
        elif y == pacY + 1:
            return pacX, 0
        elif y == pacY - 1:
            return pacX, height - 1
        else:
            return random.randint(0, width - 1), random.randint(0, height - 1)

width, height = [int(i) for i in input().split()]
grid = [input() for _ in range(height)]
myPac = {}
pac_last = {}
oppPac = {}

# 1st round record num of pac and their initial position
my_score, opponent_score = [int(i) for i in input().split()]
visible_pac_count = int(input())
for i in range(visible_pac_count):
    pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
    pac_id, x, y = int(pac_id), int(x), int(y)
    if mine != 0 and pac_id % 2 == 0:
        myPac[pac_id] = [x, y, {}, {}, 'r']
        pac_last[pac_id] = [x, y]
    elif mine != 0 and pac_id % 2 == 1:
        myPac[pac_id] = [x, y, {}, {}, 'l']
        pac_last[pac_id] = [x, y]
    elif mine == 0:
        oppPac[pac_id] = [x, y]
print(myPac, file=sys.stderr)

visible_pellet_count = int(input())
for i in range(visible_pellet_count):
    x, y, value = [int(j) for j in input().split()]
    
    for pacID, [pacX, pacY, big, small, side] in myPac.items():
        if x >= width // 2 and side == 'r':
            if value == 10:
                myPac[pacID][2][(x, y)] = pel_dis(pacX, pacY, x, y)
            else:
                myPac[pacID][3][(x, y)] = pel_dis(pacX, pacY, x, y)
                print(x, y, value, 'r', file=sys.stderr)
        elif x < width // 2 and side == 'l':
            if value == 10:
                myPac[pacID][2][(x, y)] = pel_dis(pacX, pacY, x, y)
            else:
                myPac[pacID][3][(x, y)] = pel_dis(pacX, pacY, x, y)
                print(x, y, value, 'l', file=sys.stderr)

for pacID in myPac:
    pacX, pacY, big, small, side = myPac[pacID]
    print(big, file=sys.stderr)
    print(small, file=sys.stderr)
    targetX, targetY = dission(pacX, pacY, big, small)
    print('MOVE', pacID, targetX, targetY, end='|')
print()



while True:
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())  # all your pacs and enemy pacs in sight
    for i in range(visible_pac_count):
        # pac_id: pac number (unique within a team)
        # mine: true if this pac is yours
        # x: position in the grid
        # y: position in the grid
        # type_id: unused in wood leagues
        # speed_turns_left: unused in wood leagues
        # ability_cooldown: unused in wood leagues
        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
        pac_id = int(pac_id)
        if mine != 0:
            myPac[pac_id][0], myPac[pac_id][1] = int(x), int(y)
        elif mine == 0:
            oppPac[pac_id] = [x, y]
        for pac, [pacX, pacY, big, small, side] in myPac.items():
            myPac[pac][3].pop((pacX, pacY), None)
            myPac[pac][2].pop((pacX, pacY), None)
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)
    visible_pellet_count = int(input())
    for i in range(visible_pellet_count):
        x, y, value = [int(j) for j in input().split()]
        for pacID, [pacX, pacY, big, small, side] in myPac.items():
            if x // 2 >= width and side == 'r':
                if value == 10:
                    myPac[pacID][2][(x, y)] = pel_dis(pacX, pacY, x, y)
                else:
                    myPac[pacID][3][(x, y)] = pel_dis(pacX, pacY, x, y)
            elif x // 2 < width and side == 'l':
                if value == 10:
                    myPac[pacID][2][(x, y)] = pel_dis(pacX, pacY, x, y)
                else:
                    myPac[pacID][3][(x, y)] = pel_dis(pacX, pacY, x, y)
    
    for pacID, [pacX, pacY, big, small, side] in myPac.items():
        if pacX == pac_last[pacID][0] and pacY == pac_last[pacID][1]:
            x_move, y_move = stuck(pacX, pacY, myPac)
        else:
            x_move, y_move = dission(pacX, pacY, big, small)
        pac_last[pacID] = (pacX, pacY)
        print(pacID, side, big, file=sys.stderr)
        print('MOVE', pacID, x_move, y_move, end='|')
    print()
