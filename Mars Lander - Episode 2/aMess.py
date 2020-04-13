import sys
import math


surface_n = int(input())  # the number of points used to draw the surface of Mars.
planeX, planeY = 0, 3001
height = []
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    height.append(land_y)
    if land_y == planeY:
        plane = [land_x, planeX]
        plane_h = planeY
    else:
        planeX, planeY = land_x, land_y
    
# game loop
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if y < plane_h:
        print('0 4')
        continue
    if x > max(plane) and abs(h_speed) < 30:
        acc, rotate = 4, 30
    elif x < min(plane) and abs(h_speed) < 30:
        acc, rotate = 4, -30
    else:
        if abs(h_speed) > 10:
            rotate = int(h_speed / abs(h_speed) * 30)
            acc = 4
        else:
            rotate = 0
            if abs(v_speed) > 35:
                acc = 4
            else:
                acc = 3

    print(rotate, acc)
