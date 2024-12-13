def parseMap(file):
    guardMap = []
    initialPosition = (-1, -1)
    yIdx = 0
    for line in file:
        guardMap.append(list(line.replace("\n", "")))
        xIdx = 0
        for c in line:
            if c == "^":
                initialPosition = (yIdx, xIdx)
            xIdx += 1
        yIdx += 1
    return guardMap, initialPosition

def changeDirection(direction):
    up = direction[0]
    side = direction[1]

    if up == -1:
        return (0, 1)
    
    if up == 1:
        return (0, -1)
    
    if side == 1:
        return (1, 0)
    
    if side == -1:
        return (-1, 0)
    
    raise ValueError("Direction is unexpected value!")

def checkPosition(guardMap, y, x):
    yMax = len(guardMap) - 1
    xMax = len(guardMap[0]) - 1

    if (y > yMax) or (x > xMax):
        return "Out of bounds"
    
    position = guardMap[y][x]
    if (position == ".") or (position == "^"):
        return "Clear"
    
    if position == "#":
        return "Obstructed"
    
    raise ValueError("Position is unexpected value!")

def process():
    with open('./files/day6.txt', 'r') as f: #open the file
        # Returns 2d array and tuple of (y, x)
        guardMap, position = parseMap(f)
        # Initially guard will be facing up/north
        # Direction will be a tuple of (Vertical, Horizontal)
        direction = (-1, 0)
        visited = set()
        while True:
            visited.add(position)

            nextPositionStatus = checkPosition(guardMap, position[0] + direction[0], position[1] + direction[1])

            if nextPositionStatus == "Out of bounds":
                return len(visited)

            if nextPositionStatus == "Clear":
                position = (position[0] + direction[0], position[1] + direction[1])

            if nextPositionStatus == "Obstructed":
                direction = changeDirection(direction)

    
if __name__ == "__main__":
    print("Distinct steps: " + str(process()))