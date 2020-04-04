import sys
import math

# Don't let the machines win. You are humanity's last hope...
matrix = []
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    matrix.append(line)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
output = []
counter = 0
for i in range(height):
    for j in range(width):
        if matrix[i][j] == '0':
            output = str(i) + ' ' + str(j) + ' '
            r_neighbor = False
            d_neighbor = False
            if j < width:
                for k in range(j+1, width):
                    if matrix[i][k] == '0':
                        output += str(i) + ' ' + str(k) + ' '
                        r_neighbor = True
                        break
            if not r_neighbor:
                output += str(-1) + ' ' + str(-1) + ' '
            if i < height:
                for l in range(i+1, height):
                    if matrix[l][j] == '0':
                        output += str(l) + ' ' + str(j) + ' '
                        d_neighbor = True
                        break
            if not d_neighbor:
                output += str(-1) + ' ' + str(-1) + ' '

# Three coordinates: a node, its right neighbor, its bottom neighbor
# print("0 0 1 0 0 1")\
    print(output)
