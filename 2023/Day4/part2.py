import functools
import re

data = []
with open('data.txt', 'r') as my_file:
    for line in my_file:
        data.append(re.findall("\d+", line))
        
@functools.lru_cache(maxsize=None)
def findMatches(card):
    matches = 0
    winningNums = set()
    for i in range(len(data[card])):
        # change to i < 11 for actual data
        if i < 6 and i > 0:
            winningNums.add(data[card][i])
        elif i != 0 and data[card][i] in winningNums:
            matches += 1
    for j in range(matches):
        matches += findMatches(card + j + 1)
    return matches


total = 0
for k in range(len(data)):
    total += findMatches(k) + 1

print(total)