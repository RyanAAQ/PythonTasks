def largest_number(numberone, numbertwo, numberthree):
    if (numberone > numbertwo) and (numberone > numberthree):
         return numberone

    elif (numbertwo > numberone) and (numbertwo > numberthree):
        return numbertwo

    elif (numberthree > numberone) and (numberthree > numbertwo):
        return numberthree
    
    else:
        return numberone

print("Largest =", largest_number(70, 20, 30))

