"""
    Firts collect the amount spent from the user
    Then use the if statements to check if the user enters a valid input
    then calculate the discount amount by using the user input and multiplying it by the percentage
    Then print out the result






"""
purchase_amount = int(input("Enter the amount you want to spend: "))
    
if purchase_amount >= 1000 and purchase_amount <= 10000:
    discount = purchase_amount * (5 / 100)
    print("You have a 5% discount and you saved ", discount)
    print("Your new price is ",purchase_amount - discount)

elif purchase_amount >= 10000 and purchase_amount <= 50000:
   discount2 = purchase_amount * (10 / 100)
   print("You have a 10% discount and you saved ", discount2)
   print("Your new price is ",purchase_amount - discount2)
 

else:
    discount3 = purchase_amount * (20 / 100)
    print("Your have a 20% discount and you saved ", dicount3)
    prinr("Your new price is ", purchase_amount - discount)
