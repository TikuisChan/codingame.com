n = int(input())
c = int(input())
b = sorted([int(input()) for _ in range(n)])

for i, bu in enumerate(b):
    if bu > c // n:
        b[i] = c // n
    c -= b[i]
    n -= 1

if c > 0:
    print('IMPOSSIBLE')
else:
    for bu in b:
        print(bu)
