max_tree = {}
n = int(input())
for _ in range(n):
    tele = input()
    for order, num in enumerate(tele, start=1):
        if tele[:order] not in max_tree.keys():
            max_tree[tele[:order]] = [tele[:order + 1]]

print(len(max_tree))
