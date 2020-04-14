w, h = [int(i) for i in input().split()]
wh = [list(map(int, input().split())) for _ in range(h)]  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
down = [1, 3, 7, 8, 9, 12, 13]

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    mType = wh[yi][xi]
    if mType in down:
        print(xi, yi+1)
    elif mType in [4, 5] and pos != "TOP":
        print(xi, yi+1)
    elif mType in [4, 10] and pos == "TOP":
        print(xi-1, yi)
    elif mType in [5, 11] and pos == "TOP":
        print(xi+1, yi)
    elif mType in [2, 6]:
        if pos == "LEFT":
            print(xi+1, yi)
        else:
            print(xi-1, yi)
            
