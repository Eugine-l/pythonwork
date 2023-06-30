temperature = float(input("Enter temperature value: "))
unit = input("Enter temperature unit (C or F): ")

if unit.upper() == 'C':
    # Convert Celsius to Fahrenheit
    f = (temperature * 9/5) + 32
    print(f"{temperature:.1f}°C is {f:.1f}°F in Fahrenheit.")
elif unit.upper() == 'F':
    # Convert Fahrenheit to Celsius
    c = (temperature - 32) * 5/9
    print(f"{temperature:.1f}°F is {c:.1f}°C in Celsius.")
else:
    print("Invalid unit. Please enter C or F.")
