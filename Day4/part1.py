import re

filepath = "data.txt"
with open(filepath, "r") as my_file:
    points = 0
    for line in my_file:
        x = re.findall("\d+", line)
        pointsThisCard = 0
        winningNums = set()
        for i in range (len(x)):
            if i < 11 and i > 0:
                winningNums.add(x[i])
            elif x[i] in winningNums and i != 0:
                if pointsThisCard == 0:
                    pointsThisCard = 1
                else:
                    pointsThisCard *= 2
        points += pointsThisCard
print(points)