import re

lines = []
with open('data.txt', 'r') as my_file:
    for line in my_file:
        lines.append(list(line.strip()))

isGear = r"(\*)|(\?\d+)"
sum = 0
linesLen = len(lines)
for y in range(linesLen):
    line = lines[y]
    lineLen = len(line)
    currNum = ''
    gearAroundNum = (-1, -1)

    for x in range(lineLen):
        c = line[x]
        try:
            int(c)
            currNum += c

            charsToCheck = {
                (lines[y-1][x], y-1, x) if y != 0 else ('.', -1, -1),
                (lines[y+1][x], y+1, x) if y != len(lines) - 1 else ('.', -1, -1),
                (lines[y-1][x-1], y-1, x-1) if y != 0 and x != 0 else ('.', -1, -1),
                (lines[y+1][x-1], y+1, x-1) if y != len(lines) - 1 and x != 0 else ('.', -1, -1),
                (lines[y-1][x+1], y-1, x+1) if y != 0 and x != len(line) - 1 else ('.', -1, -1),
                (lines[y+1][x+1], y+1, x+1) if y != len(lines) - 1 and x != len(line) - 1 else ('.', -1, -1),
                (lines[y][x-1], y, x-1) if x != 0 else ('.', -1, -1),
                (lines[y][x+1], y, x+1) if x != len(line) - 1 else ('.', -1, -1)
            }

            for triple in charsToCheck:
                if gearAroundNum != (-1, -1):
                    break
                char, yChar, xChar = triple
                if bool(re.search(isGear, char)):
                    gearAroundNum = (yChar, xChar)
            if x == lineLen - 1 and gearAroundNum != (-1, -1):
                gearSpot = lines[gearAroundNum[0]][gearAroundNum[1]]
                if gearSpot == '*':
                    lines[gearAroundNum[0]][gearAroundNum[1]] = '?' + currNum
                else:
                    otherNum = int(gearSpot[1:])
                    sum += otherNum * int(currNum)
        except ValueError:
            if currNum != '' and gearAroundNum != (-1, -1):
                gearSpot = lines[gearAroundNum[0]][gearAroundNum[1]]
                if gearSpot == '*':
                    lines[gearAroundNum[0]][gearAroundNum[1]] = '?' + currNum
                else:
                    otherNum = int(gearSpot[1:])
                    sum += otherNum * int(currNum)

            gearAroundNum = (-1, -1)
            currNum = ''

print(sum)