import re

lines = []
with open('data.txt', 'r') as my_file:
    for line in my_file:
        lines.append(list(line.strip()))

isSymbol = r"[^\d\.]"
sum = 0
linesLen = len(lines)
for y in range(linesLen):
    line = lines[y]
    lineLen = len(line)
    currNum = ''
    symbolAroundNum = False

    for x in range(lineLen):
        c = line[x]
        try:
            int(c)
            currNum += c

            charsToCheck = {
                lines[y-1][x] if y != 0 else '.',
                lines[y+1][x] if y != len(lines) - 1 else '.',
                lines[y-1][x-1] if y != 0 and x != 0 else '.',
                lines[y+1][x-1] if y != len(lines) - 1 and x != 0 else '.',
                lines[y-1][x+1] if y != 0 and x != len(line) - 1 else '.',
                lines[y+1][x+1] if y != len(lines) - 1 and x != len(line) - 1 else '.',
                lines[y][x-1] if x != 0 else '.',
                lines[y][x+1] if x != len(line) - 1 else '.'
            }

            for char in charsToCheck:
                if symbolAroundNum:
                    break
                symbolAroundNum = bool(re.search(isSymbol, char))
            if x == lineLen - 1 and symbolAroundNum:
                sum += int(currNum)
        except ValueError:
            if currNum != '' and symbolAroundNum:
                sum += int(currNum)

            symbolAroundNum = False
            currNum = ''

print(sum)

