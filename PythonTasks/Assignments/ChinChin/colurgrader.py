import random

number = random.randint(1, 7)

if number == 1:
    colour = "Violet"

elif number == 2:
    colour = "Indigo"

elif number == 3:
    colour = "Blue"

elif number == 4:
    colour = "Green"

elif number == 5:
    colour = "Yellow"

elif number == 6:
    colour = "Orange"

else: 
    colour = "Red"

print(number, "=", colour)
