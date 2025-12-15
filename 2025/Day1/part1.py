def rotate(currentVal: int, dist: int, direction: str):
    if(direction == "L"):
        return (currentVal - dist) % 100
    elif(direction == "R"):
        return (currentVal + dist) % 100
    else:
        raise ValueError("Invalid direction.")

def main():
    with open("inputValues.txt", "r", encoding="utf-8") as f:
        text = f.read()

    currentVal = 50
    hits = 0

    for line in text.splitlines():
        if(line[0] not in ("L", "R")):
            raise ValueError("Direction of turn is not specified")
        else:
            turnDistance = int(line[1:])
        currentVal = rotate(currentVal, turnDistance, line[0])
        if(currentVal == 0):
            hits += 1
    print(f"Amount of times 0 was hit: {hits}")

if __name__ == "__main__":
    main()