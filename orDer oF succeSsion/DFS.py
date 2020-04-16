def printName(start):
    if start[3] == '-' and start[4] != 'Catholic':
        print(start[0])
    if len(tree[start[0]][0]) > 0:
        for childM in tree[start[0]][0]:
            printName(childM)
    if len(tree[start[0]][1]) > 0:    
        for childF in tree[start[0]][1]:
            printName(childF)

tree = {}
all_ppl = []
n = int(input())
for i in range(n):
    ppl = input().split()
    if ppl[0] not in tree.keys():  # add nodes by name as keys
        tree[ppl[0]] = [[], []]
    all_ppl.append(ppl)

for parent in tree:
    for ppl in all_ppl:
        if ppl[1] == parent and ppl[-1] == 'M':
            tree[parent][0].append(ppl)
        elif ppl[1] == parent and ppl[-1] == 'F':
            tree[parent][1].append(ppl)
        elif ppl[1] == '-':
            root = ppl

for parent in tree:
    tree[parent][0] = sorted(tree[parent][0], key=lambda x: x[2])
    tree[parent][1] = sorted(tree[parent][1], key=lambda x: x[2])

printName(root)
