points = {
          'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1, 
          'd': 2, 'g': 2, 
          'b': 3, 'c': 3, 'm': 3, 'p': 3,
          'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 
          'k': 5, 
          'j': 8, 'x': 8, 
          'q': 10, 'z': 10
         }
notMatch = []

n = int(input())
w = [input() for _ in range(n)]
letters = input()

for word in w:
    letter_cp = list(letters)
    for letter in word:
        if letter not in letter_cp:
            notMatch.append(word)
            break
        else:
            letter_cp.remove(letter)

for word in notMatch:
    if word in w:
        w.remove(word)

if len(w) == 1:
    ans = w[0]
else:
    ans, highest = '', 0
    for word in w:
        score = 0
        for letter in word:
            score += points[letter]
        if highest < score:
            ans, highest = word, score

print(ans)
