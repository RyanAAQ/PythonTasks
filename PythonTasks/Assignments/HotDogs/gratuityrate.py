subtotal = float(input("Enter the subtotal: "))
gratuityrate = float(input("Enter the gratuity rate (%): "))
gratuity = subtotal * (gratuityrate / 100)
total = subtotal + gratuity

print("Gratutity = $",gratuity)
print("Total = $",total)
