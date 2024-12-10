def parse2dXmas(file):
    xmas = []
    for line in file:
        xmas.append(list(line))
    return xmas

def searchUp(xmas2d, y, x):
    sum = 0
    if(y-3 >= 0):
        m = xmas2d[y-1][x] == "M"
        a = xmas2d[y-2][x] == "A"
        s = xmas2d[y-3][x] == "S"
        if m and a and s:
            sum += 1
    yLen = len(xmas2d)
    if(y+3 < yLen):
        m = xmas2d[y+1][x] == "M"
        a = xmas2d[y+2][x] == "A"
        s = xmas2d[y+3][x] == "S"
        if m and a and s:
            sum +=1
    return sum

def searchDown(xmas2d, y, x):
    y

def searchRight(xmas2d, y, x):
    sum = 0
    if(x-3 >= 0):
        m = xmas2d[y][x-1] == "M"
        a = xmas2d[y][x-2] == "A"
        s = xmas2d[y][x-3] == "S"
        if m and a and s:
            sum += 1
    xLen = len(xmas2d[y])
    if(x+3 < xLen):
        m = xmas2d[y][x+1] == "M"
        a = xmas2d[y][x+2] == "A"
        s = xmas2d[y][x+3] == "S"
        if m and a and s:
            sum += 1
    return sum

def searchDiagonal(xmas2d, y, x):
    xLen = len(xmas2d[y])
    yLen = len(xmas2d)
    sum = 0
    if x-3 >= 0:
        if y-3 >= 0: # up left
            m = xmas2d[y-1][x-1] == "M"
            a = xmas2d[y-2][x-2] == "A"
            s = xmas2d[y-3][x-3] == "S"
            if m and a and s:
                sum += 1
        if y+3 < yLen: # down left
            m = xmas2d[y+1][x-1] == "M"
            a = xmas2d[y+2][x-2] == "A"
            s = xmas2d[y+3][x-3] == "S"
            if m and a and s:
                sum += 1
    if x+3 < xLen: 
        if y-3 >= 0: # up right
            m = xmas2d[y-1][x+1] == "M"
            a = xmas2d[y-2][x+2] == "A"
            s = xmas2d[y-3][x+3] == "S"
            if m and a and s:
                sum += 1
        if y+3 < yLen: # down right
            m = xmas2d[y+1][x+1] == "M"
            a = xmas2d[y+2][x+2] == "A"
            s = xmas2d[y+3][x+3] == "S"
            if m and a and s:
                sum += 1
    return sum

def searchFromX(xmas2d, y, x):
    xmas = 0
    xmas += searchUp(xmas2d, y, x)
    xmas += searchRight(xmas2d, y, x)
    xmas += searchDiagonal(xmas2d, y, x)
    return xmas
    
with open('./files/day4.txt', 'r') as f: #open the file
    totalXmas = 0
    xmas2d = parse2dXmas(f)
    for y in range(0, len(xmas2d)):
        for x in range(0, len(xmas2d[y])):
            if xmas2d[y][x] == "X":
                totalXmas += searchFromX(xmas2d, y, x)
    print(totalXmas)
