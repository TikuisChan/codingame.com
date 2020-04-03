import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
h_min, h_max = 0, h
w_min, w_max = 0, w

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if 'U' in bomb_dir:
        h_max = y0
    elif 'D' in bomb_dir:
        h_min = y0
    else:
        pass
    
    y = (h_max + h_min) // 2
    y0 = y
    if 'R' in bomb_dir:
        w_min = x0
    elif 'L' in bomb_dir:
        w_max = x0
    else:
        pass
    
    x = (w_max + w_min) // 2
    x0 = x
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    # the location of the next window Batman should jump to.
    print(x, y)
