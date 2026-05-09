number = int(input("Enter a 3 digit number: "))
firstdigit = number / 100
lastdigit = number % 10

if firstdigit == lastdigit:
    print(number, " is a palindrome")

else:
    print(number, "is not a palindrome")
