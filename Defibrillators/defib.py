import math

def dist(lonA, latA, lonB, latB):
    x = (lonB - lonA) * math.cos((latA + latB) / 2)
    y = (latB - latA)
    return math.sqrt(x ** 2 + y ** 2) * 6371

lon = math.radians(float(input().replace(',', '.')))
lat = math.radians(float(input().replace(',', '.')))
n = int(input())
ans = ''
min_dist = 1000000
for i in range(n):
    defib = input()
    defib_sp = defib.replace(',', '.').split(';')
    lonB = math.radians(float(defib_sp[-2]))
    latB = math.radians(float(defib_sp[-1]))
    if dist(lon, lat, lonB, latB) < min_dist:
        ans = defib_sp[1]
        min_dist = dist(lon, lat, lonB, latB)
    
print(ans)
