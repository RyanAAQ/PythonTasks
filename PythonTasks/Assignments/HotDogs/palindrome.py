number = int(input("Enter a three digit number: "))
firstdigit = number // 100
lastdigit = number % 10

if firstdigit == lastdigit:
    print(number, "is a palindrome")

else:
    print(number, "is not a prime number")
