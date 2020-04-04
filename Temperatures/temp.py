import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())  # the number of temperatures to analyse

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
if n == 0:
    print(0)
else:
    t = []
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t.append(int(i))
    ans = sorted(t, key=abs)[0]
    if abs(ans) in t:
        print(abs(ans))
    else:
        print(ans)
