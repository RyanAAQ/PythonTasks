print("number\tsquare\tcube")

for number in range(6):
    squares = number ** 2
    cubes = number ** 3
    print(f"{number:>6}\t{square:>6}\t{cube:>4}")
