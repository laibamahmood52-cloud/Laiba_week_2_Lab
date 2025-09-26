correct_password = "python123"

while True:
    attempts = 3

    while attempts > 0:
        password = input("Enter password: ")
        if password == correct_password:
            print("Access granted!")
            exit()
        else:
            attempts -= 1
            print(f"Incorrect. {attempts} attempts left.")

    # After 3 failed attempts
    print("Access denied. Too many failed attempts.")

    reset_choice = input("Do you want to reset your password? (yes/no): ").lower()
    if reset_choice == "yes":
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")
        if new_password == confirm_password:
            correct_password = new_password
            print("Password reset successful. Try logging in again.\n")
        else:
            print("Passwords do not match. Password not reset.\n")
    else:
        print("Exiting program.")
        break
