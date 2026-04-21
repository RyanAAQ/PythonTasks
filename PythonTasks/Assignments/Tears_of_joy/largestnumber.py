number = input("Enter number: ")
largest = number

while number != "done":
    if number > largest:
        largest = number
    number = input("Enter number: ")

print("Largest =", largest)

    

