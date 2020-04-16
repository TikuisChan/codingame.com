def printName(start):
    if start[3] == '-' and start[4] != 'Catholic':
        print(start[0])
    if len(tree[start[0]]) > 0:
        for child in tree[start[0]]:
            printName(child)

tree = {}
all_ppl = []
n = int(input())
for i in range(n):
    ppl = input().split()
    if ppl[0] not in tree.keys():  # add nodes by name as keys
        tree[ppl[0]] = []
    all_ppl.append(ppl)

for parent in tree:
    for ppl in all_ppl:
        if ppl[1] == parent:
            tree[parent].append(ppl)
        elif ppl[1] == '-':
            root = ppl

for parent in tree:
    tree[parent] = sorted(tree[parent], key=lambda x: (x[-1] == 'F', x[2]))

printName(root)
