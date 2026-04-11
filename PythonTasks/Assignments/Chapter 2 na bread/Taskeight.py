principal = int(input("Enter the principal: "))
rate = int(input("Enter the interest rate in %: "))
time = int(input("Enter the time in years: "))

SI = (principal * (rate / 100) * time ) / 100
totalamount = principal + SI

print("The simple interest is ", SI)
print("And the total amount is ", totalamount)
