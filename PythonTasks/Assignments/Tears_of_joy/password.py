attempts = 0
print("ZENITH BANK OF NIGERIA")
print("-"* 15)

while attempts < 3:
    password = input("Password: ")
    if password == "python123":
        print("Access granted")
        break
    attempts += 1
else:
    print("Locked out :(")
    print("Thief dey go :O")

