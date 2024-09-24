
'''def sign_in_simulation():
    # Predefined username and password
    correct_username = "MANASA"
    correct_password = "1234"

    print("Welcome to the Sign-In Page")

    # Get user input
    username = input("Enter your username: ").strip().upper()
    password = input("Enter your password: ")

    # Check if the credentials are correct
    if username == correct_username and password == correct_password:
        print("Sign-in successful!")
    else:
        print("Invalid username or password. Please try again.")

# Run the sign-in simulation
if __name__ == "__main__":
    sign_in_simulation()'''


def sign_in_simulation():
    # Predefined username and password
    correct_username = "MANASA"
    correct_password = "1234"

    print("Welcome to the Sign-In Page")

    for attempt in range(2):  # Allow 2 attempts in total
        # Get user input
        username = input("Enter your username: ").strip().upper()  # Normalize username
        password = input("Enter your password: ")

        # Basic validation for empty input
        if not username or not password:
            print("Username and password cannot be empty. Please try again.")
            continue

        # Check if the credentials are correct
        if username == correct_username and password == correct_password:
            print("Sign-in successful!")
            return  # Exit the function on successful sign-in
        else:
            if attempt < 1:  # If not the last attempt
                print("Invalid username or password. Please try again.")
            else:
                print("Invalid username or password. No attempts remaining.")
    print("Sign-In failed please contact the customer support!")

# Run the sign-in simulation
if __name__ == "__main__":
    sign_in_simulation()
