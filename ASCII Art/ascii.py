def char2art(char, w, h, row):
    charMap = 'abcdefghijklmnopqrstuvwxyz?'
    charPos = charMap.find(char.lower())
    if charPos != -1:
        return [x[charPos * w: (charPos * w) + w] for x in row]
    else:
        return [x[- w:] for x in row]


l = int(input())
h = int(input())
t = input()
row = [input() for _ in range(h)]
ans = [[] for _ in range(h)]
for char in t:
    charArt = char2art(char, l, h, row)
    i = 0
    for n in ans:
        n += charArt[i]
        i += 1

for line in ans:
    print(''.join(line))
