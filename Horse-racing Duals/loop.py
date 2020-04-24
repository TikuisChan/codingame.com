n = int(input())
pi = sorted([int(input()) for _ in range(n)])
diff = 10000000
for i, strength in enumerate(pi):
    diff = min(abs(diff), pi[i] - pi[i-1])
print(diff)
