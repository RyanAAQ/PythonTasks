print(" " * 3, end="")
for number in range(1, 10):
    print(f"{number:4}", end="")
print("\n" + " " * 3 + "-" * 40)

for count in range(1, 10):
    print(f"{count:2}|", end=" ")

    for column in range(1, 10):
        multiple = count * column
        print(f"{multiple:4}", end="") 

    print()

