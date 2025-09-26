fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"Converted temperature: {celsius:.2f}°C")

if celsius > 50 or celsius < 30:
        print("Warning: Temperature is too extreme.")
elif celsius >= 37:
        print("Grade: A")
elif celsius >= 30:
        print("Grade: B")
else:
        print("Grade: F")