number = int(input("Enter a five-digit integer: "))

if 10000 <= number <= 99999:
    reversednumber = 0
    newnumber = number

    while newnumber > 0:
        digit = newnumber % 10 
        reversednumber = (reversednumber * 10) + digit
        newnumber //= 10

    if number == reversednumber:
        print(number, "is a palindrome")
    else:
        print(number ,"is not a palindrome")

