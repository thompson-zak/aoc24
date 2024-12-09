import re

def parseFileDos(file):
    commands = ""
    for line in file:
        commands += line
    dontSections = commands.split("don't()")
    for i in range(1, len(dontSections)):
        dontSections[i] = "don't()" + dontSections[i]
    doSections = []
    for dontSection in dontSections:
        doSection = dontSection.split("do()")
        if dontSection[0:4] == "do()":
            start = 0
        else:
            start = 1
        for i in range(start, len(doSection)):
            doSection[i] = "do()" + doSection[i]
        doSections.append(doSection)
    return doSections

def sumSubtring(substring):
    sum = 0
    mulCommands = re.findall(r'mul\(([0-9]+),([0-9]+)\)', substring)
    for mulCommand in mulCommands:
        sum += int(mulCommand[0]) * int(mulCommand[1])
    return sum

with open('./files/day3.txt', 'r') as f: #open the file
    sum = 0
    commands2d = parseFileDos(f)
    do = True
    for commands in commands2d:
        for command in commands:
            if(command.startswith("don't()")):
                do = False

            if(command.startswith("do()")):
                do = True

            if do:
                sum += sumSubtring(command)
    print(sum)