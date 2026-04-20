print('Enter two numbers and imma tell you the relationships that they satisfy')

number_1 = int(input("Enter first number: "))

number_2 = int(input("Enter second number: "))

if number_1 == number_2:
    print(number_1, 'is equal to', number_2)

else:
    print(number_1, 'is not equal to', number_2)

if number_1 < number_2:
    print(number_1, 'is less than', number_2)

else:
    print(number_1, 'is greater than', number_2)

if number_1 <= number_2:
    print(number_1, 'is less than or equal to', number_2)

else:
    print(number_1, 'is greater than or equal to', number_2)
