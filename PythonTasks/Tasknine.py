seconds = int(input("Enter the number of seconds"))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print("The number is ", hours, "Hours ", minutes, "Minutes and", seconds, "Seconds")
