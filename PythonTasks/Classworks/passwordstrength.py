#collect the password from the user
#check the password length
#and use the selection statements to determine how long the password is and its streangth


password = (input("Enter your password: "))
  
if (len(password)) < 8:
    print("Strength: Very weak") 

elif (len(password)) == 8:
    print("Strength: Weak")

elif (len(password)) >= 8 and (len(password)) <= 16:
    print("Strength: Strong")

else:
    print("Strength: Very strong nga")

