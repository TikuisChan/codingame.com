def conwayNext(r):
    nextline = []
    num_char = 0
    char = r[0]
    for num in r:
        if num == char:
            num_char += 1
        else:
            nextline.append(num_char)
            nextline.append(char)
            char = num
            num_char = 1
    nextline.append(num_char)
    nextline.append(char)
    return nextline

r = [int(input())]
l = int(input())

for i in range(l-1):
    r = conwayNext(r)

r = list(map(str, r))

print(' '.join(r))
