import sys
import math


def cableLength(y, houses):
    length = 0
    houses = sorted(houses, key=lambda x: x[0])
    length += houses[-1][0] - houses[0][0]
    for house in houses:
        length += abs(house[1] - y)
    return length

def mean(houses):
    mean = 0
    for i in range(n):
        mean += houses[i][1]
    return round(mean / n)
    
def median(houses):
    houses = sorted(houses, key=lambda x: x[1])
    if len(houses) % 2 == 1:
        return houses[n // 2][1]
    else:
        return round(houses[n // 2][1] + houses[n // 2 - 1][1])
    
n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]
ans = min(cableLength(mean(houses), houses), cableLength(median(houses), houses))

print(ans)
