numberone = float(input("Enter first number: "))
numbertwo = float(input("Enter second number: "))
numberthree = float(input("Enter third number: "))

if numberone == 0:
    print("No solution")

else:
    total = (numberthree - numbertwo) / numberone
    print("Answer =", total)   
