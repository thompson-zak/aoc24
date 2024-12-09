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

def getOccurrences(columnB):
    occurrences = {}
    for entry in columnB:
        occurrences[entry] = occurrences.get(entry, 0) + 1
    return occurrences


with open('./files/day1.txt', 'r') as f: #open the file
    similarity_score = 0
    columnA, columnB = getColumns(f)
    occurrences = getOccurrences(columnB)
    for entry in columnA:
        occurrence = occurrences.get(entry, 0)
        similarity_score += entry * occurrence
    print(similarity_score)