def temperature_converter(celcius):
    return ((9 / 5 ) * celcius + 32)
    

for number in range(101):
    print(f"\t{number} Fahrenheit =\t{temperature_converter(number)} Celcius")
