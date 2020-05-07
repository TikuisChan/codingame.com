sudoku = [input().split() for i in range(9)]
ans = ('true', 'false')
n = 0
for row in sudoku:
    for i in row:
        if row.count(i) > 1:
            n = 1

for i in range(9):
    check = list(range(1, 10))
    for j in range(9):
        try:
            check.remove(int(sudoku[j][i]))
        except:
            n = 1

counter = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
for i in range(3):
    for j in range(3):
        check = list(range(1, 10))
        for count in counter[i]:
            for c in counter[j]:
                try:
                    check.remove(int(sudoku[count][c]))
                except:
                    n = 1
print(ans[n])
