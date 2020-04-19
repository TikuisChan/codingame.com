def DFS(start, longest=[], path=[]):
    path = path + [start]
    if start not in tree.keys():
        return path
    for node in tree[start]:
        newPath = DFS(node, longest, path)
        if newPath != None and len(longest) < len(newPath):
            longest = newPath
    return longest
    
tree = {}
mentors = []
mentee = []
n = int(input())  # the number of relationships of influence
for i in range(n):
    x, y = [int(j) for j in input().split()]
    if x not in mentors:
        mentors.append(x)
    if y not in mentee:
        mentee.append(y)
    if x not in tree.keys():
        tree[x] = [y] 
    else:
        tree[x].append(y)

for x in mentors:
    if x in mentee:
        mentors.remove(x)

print(max([len(DFS(x)) for x in mentors]))
