import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
v = [int(x) for x in input().split()]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

v_max = v[0]
i = 0
p_max = 0

while i <= n - 1:
    if v[i] > v_max:
        v_max = v[i]
    elif v[i] - v_max < p_max:
        p_max = v[i] - v_max
    i += 1

print(p_max)
