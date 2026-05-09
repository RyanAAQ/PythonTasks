monthlyrate = 0.003125
monthlysavings = int(input("Enter your monthly savings amount: "))
accountvalue = 0.0

for month in range(1, 7):
    accountvalue = (accountvalue + monthlysavings) * (1 + monthlyrate)
print("After 6 months, the amount =", accountvalue)

