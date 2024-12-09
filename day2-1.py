def getReports(file):
    reports = []
    for line in file:
        report = line.split(" ")
        reports.append([int(level) for level in report])
    return reports

with open('./files/day2.txt', 'r') as f: #open the file
    safe_count = 0
    reports = getReports(f)
    #reports = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
    for report in reports:
        isIncreasing = report[0] < report[1]
        firstLevel = report[0]
        isSafe = True
        for i in range(1, len(report)):
            if isIncreasing:
                correctOrder = report[i] > firstLevel
                difference = report[i] - firstLevel
            else:
                correctOrder = report[i] < firstLevel
                difference = firstLevel - report[i]
            safeDiff = difference >= 1 and difference <= 3
            if((not correctOrder) or (not safeDiff)):
                isSafe = False
            firstLevel = report[i]
        if isSafe:
            safe_count += 1
    print(safe_count)