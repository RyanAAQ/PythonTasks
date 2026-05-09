import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = math.pi * radius ** 2 * height
surfacearea = 2 * math.pi * radius * height + (2 * math.pi * radius ** 2)

print("Volume =", volume)
print("Surface area =", surfacearea)
