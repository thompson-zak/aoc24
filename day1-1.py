def getColumns(file):
    columnA = []
    columnB = []
    for line in file:
        split = line.split("   ")
        columnA.append(int(split[0]))
        columnB.append(int(split[1]))
    columnA.sort()
    columnB.sort()
    return columnA, columnB

with open('./files/day1.txt', 'r') as f: #open the file
    total_distance = 0
    columnA, columnB = getColumns(f)
    for i in range(0, len(columnA)):
        total_distance += abs(columnA[i]-columnB[i])
    print(total_distance)