def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
        
    return y
    
    
print(mystery([1, 2, 3, 4, 5]))

#this adds the square of the numbers in the argument together
