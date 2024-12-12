def parseRulesAndUpdates(file):
    rules = {}
    for line in file:
        if len(line.strip()) == 0:
            break
        before, after = [int(x) for x in line.split("|")]
        if before not in rules:
            rules[before] = set()
        rules[before].add(after)

    updates2d = []
    for line in file:
        intUpdates = [int(item) for item in line.split(",")]
        updates2d.append(intUpdates)

    return rules, updates2d


with open('./files/day5.txt', 'r') as f: #open the file
    middle_page_sum = 0
    #rules = {75: [47, 61, 53, 29], 47: [61, 53, 29], 97: [75]}
    #updates2d = [[75,47,61,53,29], [75,97,47,61,53]]
    rules, updates2d = parseRulesAndUpdates(f)
    for updates in updates2d:
        isOrdered = True
        for i in range(len(updates)-1, 0, -1):
            rule = rules.get(updates[i], [])
            for j in range(i-1, -1, -1):
                if updates[j] in rule:
                    isOrdered = False
                    break
            if not isOrdered:
                break
        if isOrdered:
            middle_page_sum += updates[len(updates)//2]
    print(middle_page_sum)

