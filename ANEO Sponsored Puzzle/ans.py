import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

speed = int(input())
light_count = int(input())
light = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    light.append([distance, duration])

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for _ in range(speed):
    pass_through = True
    spd_ms = speed * 1000 / 3600
    for i in range(light_count):
        arrive_time = round(light[i][0] / spd_ms)
        det = round(arrive_time % (2 * light[i][1]))
        if det >= light[i][1] and det <= 2 * light[i][1]:
            print(speed, det, light[i][1], i, file=sys.stderr)
            pass_through = False
            break
    if pass_through:
        answer = speed
        break
    speed -= 1

print(answer)
