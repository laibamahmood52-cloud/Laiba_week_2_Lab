try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Error: Age cannot be negative.")
    elif age >= 65:
        print("You are eligible to vote.")
        print("You are classified as a senior citizen.")
    elif age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
except ValueError:
    print("Invalid input. Please enter a valid age as a number.")
