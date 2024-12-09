import re

def stringifyFile(file):
    commands = ""
    for line in file:
        commands += line
    return commands

with open('./files/day3.txt', 'r') as f: #open the file
    sum = 0
    commands = stringifyFile(f)
    #commands = "mul(12,15)"
    mulCommands = re.findall(r'mul\(([0-9]+),([0-9]+)\)', commands)
    for mulCommand in mulCommands:
        sum += int(mulCommand[0]) * int(mulCommand[1])
    print(sum)