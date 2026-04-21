total = 0
count = 0

while True:
    num = float(input("Enter a number: "))
    if num == -1:
        break
    total += num
    count += 1

if count > 0:
    print("Count:", count, "Average:", total / count)

