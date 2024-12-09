def getReports(file):
    reports = []
    for line in file:
        report = line.split(" ")
        reports.append([int(level) for level in report])
    return reports

def isReportSafe(report):
    isIncreasing = report[0] < report[1]
    firstLevel = report[0]
    isSafe = True
    incorrectIdx = -1
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
            incorrectIdx = i-1
        firstLevel = report[i]
    return isSafe, incorrectIdx

with open('./files/day2.txt', 'r') as f: #open the file
    safe_count = 0
    reports = getReports(f)
    #reports = [[1, 3, 2, 4, 5], [8, 6, 4, 4, 1]]
    for report in reports:
        isSafe, incorrectIdx = isReportSafe(report)
        if isSafe:
            safe_count += 1
        else:
            for i in range(0, len(report)):
                reportCopy = [elem for elem in report]
                reportCopy.pop(i)
                isPermuationSafe, _ = isReportSafe(reportCopy)
                if isPermuationSafe:
                    safe_count += 1
                    break
    print(safe_count)