num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

minimum = num1
maximum = num1

print('The sum is', (num1 + num2 + num3))
print('The average is', (num1 + num2 + num3) / 3)
print('The product is', (num1 * num2 * num3))

if num2 < minimum:
    minimum = num2

if num3 < minimum:
    minimum = num3

print('The minimum number is', minimum)

if num2 > maximum:
    maximum = num2

if num3 > maximum:
    maximum = num3

print('The maximum number is', maximum)
