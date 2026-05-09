velocity = int(input("Enter the initial velocity: "))
time = int(input("Enter the time span: "))
acceleration = int(input("Enter the acceleration: "))
distance = (velocity * time) + 0.5 * acceleration * time ** 2

print("The distance covered =",distance, "miles")
