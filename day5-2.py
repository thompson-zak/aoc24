import pprint

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

def findIncorrect(updates, i, rules):
    update = updates[i]
    if update not in rules:
        return -1
    for j in range(i):
        if updates[j] in rules[update]:
            return j
    return -1

def sort(updates, rules, step = 0):
    for i in range(len(updates)):
        j = findIncorrect(updates, i, rules)
        if j != -1:
            sorted = updates[:j] + updates[i:i+1] + updates[j:i] + updates[i+1:]
            return sort(sorted, rules, step+1)
    
    if step == 0:
        return [0]
    else:
        return updates

def process():
    with open('./files/day5.txt', 'r') as f: #open the file
        middle_page_sum = 0
        rules, updates2d = parseRulesAndUpdates(f)
        sortedUpdates2d = []
        for updates in updates2d:
            sortedUpdates = sort(updates, rules)
            sortedUpdates2d.append(sortedUpdates)

        pprint.pprint(sortedUpdates2d)

        for sortedUpdates in sortedUpdates2d:
            middle_page_sum += sortedUpdates[len(sortedUpdates)//2]

        print(middle_page_sum)

if __name__ == "__main__":
    process()