number = int(input("Enter the number: "))
sumofnumber = 0
digits = number

while(digits > 0):
    sumofnumber += digits % 10
    digits /= 10

print("Sum of the digits =", sumofnumber)
