import re

sum = 0
filepath = "data.txt"
with open(filepath, "rt") as my_file:
    for line in my_file:
        reggie = "\d"
        x = re.findall(reggie, line)
        sum += int(x[0]+x[-1])
print(sum)