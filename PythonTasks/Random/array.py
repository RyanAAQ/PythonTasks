def largeminussmall(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers:
       if number > largest:
            largest = number
       if number < smallest:
          smallest = number
    return largest - smallest        
 
 
numbers = [1, 4, 7, 9, 10]
print(largeminussmall(numbers))    
