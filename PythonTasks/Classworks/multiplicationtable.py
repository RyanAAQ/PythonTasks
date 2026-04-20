"""Collect input from user
Use a for loop to print out the table
implement the users input with the table
Then calculate the total answer
"""

number = int(input("Enter a number: "))

for num in range(1, 11):
    print(number, "X", num, " = ", (num * number))


