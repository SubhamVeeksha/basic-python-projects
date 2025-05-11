def convert_temperature():
    temp = float(input("Enter temperature value: "))
    scale_from = input("Enter the scale to convert from (C, F, K): ").upper()
    scale_to = input("Enter the scale to convert to (C, F, K): ").upper()

    if scale_from == 'C':
        if scale_to == 'F':
            print(f"{temp}°C is {(temp * 9/5) + 32}°F")
        elif scale_to == 'K':
            print(f"{temp}°C is {temp + 273.15}K")
    elif scale_from == 'F':
        if scale_to == 'C':
            print(f"{temp}°F is {(temp - 32) * 5/9}°C")
        elif scale_to == 'K':
            print(f"{temp}°F is {(temp - 32) * 5/9 + 273.15}K")
    elif scale_from == 'K':
        if scale_to == 'C':
            print(f"{temp}K is {temp - 273.15}°C")
        elif scale_to == 'F':
            print(f"{temp}K is {(temp - 273.15) * 9/5 + 32}°F")
    else:
        print("Invalid scale input!")

# Call the function
convert_temperature()
