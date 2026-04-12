principal = int(input("Enter the principal: "))
rate = int(input("Enter the interest rate in %: "))
duration = int(input("Enter the duration of the loan: "))

nrate = rate / 100
nduration = duration / 12

mortgage = (principal * (nrate *(1 + nrate) ** duration) / ((1 + nrate) ** duration) - 1)
 

print(mortgage)
