def parse2dXmas(file):
    xmas = []
    for line in file:
        xmas.append(list(line))
    return xmas

def searchFromA(xmas2d, y, x):
    xLen = len(xmas2d[y])
    yLen = len(xmas2d)
    sum = 0

    right = x+1 < xLen
    left = x-1 >= 0
    up = y-1 >= 0
    down = y+1 < yLen

    if right and left and up and down:
        leftSM = xmas2d[y-1][x-1] == "S" and xmas2d[y+1][x+1] == "M"
        leftMS = xmas2d[y-1][x-1] == "M" and xmas2d[y+1][x+1] == "S"

        rightSM = xmas2d[y+1][x-1] == "S" and xmas2d[y-1][x+1] == "M"
        rightMS = xmas2d[y+1][x-1] == "M" and xmas2d[y-1][x+1] == "S"
        
        if (rightSM or rightMS) and (leftSM or leftMS):
            sum += 1
    return sum

with open('./files/day4.txt', 'r') as f: #open the file
    totalXmas = 0
    xmas2d = parse2dXmas(f)
    #xmas2d = [["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]]
    for y in range(0, len(xmas2d)):
        for x in range(0, len(xmas2d[y])):
            if xmas2d[y][x] == "A":
                totalXmas += searchFromA(xmas2d, y, x)
    print(totalXmas)