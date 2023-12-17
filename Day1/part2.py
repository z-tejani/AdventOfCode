import re

sum = 0
numbers = {
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}
reggie = "(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))"
filepath = "data.txt"
linenum = 1
with open(filepath, "rt") as my_file:
    for line in my_file:
        x = re.findall(reggie, line)
        if x[0] in numbers:
            x[0] = str(numbers[x[0]])
        if x[-1] in numbers:
            x[-1] = str(numbers[x[-1]])
        print(f"{linenum:<5}: {str(x):<75} OUT: {int(x[0]+x[-1])}")
        sum += int(x[0]+x[-1])
        linenum += 1
print(f"SUM: {sum}")
