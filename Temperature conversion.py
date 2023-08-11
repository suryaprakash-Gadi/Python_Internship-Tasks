
print("Temperature Conversion")
print("----------------------")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")

if unit.lower() == "c":
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {converted_temperature}°F")

elif unit.lower() == "f":
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {converted_temperature:.2f}°C")

else:
    print("Invalid unit of measurement please enter (c or f).")
