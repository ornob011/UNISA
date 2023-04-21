#
# File: tabcy007_converter.py
# Author: Chowdhury Nabila Tabassum
# Email Id: tabcy007@mymail.unisa.edu.au
# Description: Assignment 1 – menu driven program called tabcy007_converter.py that will allow the user to enter commands and process these commands until the quit command is entered. The program will accept entry of a number (in either decimal or binary notation) from the keyboard and convert it to either binary or decimal notation as requested.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#


# Function definitions
def display_details():  # Display the program details
    print("File : tabcy007_converter.py")
    print("Author : Chowdhury Nabila Tabassum")
    print("Stud ID : 110405435")
    print("Email ID : tabcy007@mymail.unisa.edu.au")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")


def get_menu_choice():  # Display the menu and get the user's choice
    print("\n*** Menu ***\n")
    print("1. Convert to binary")
    print("2. Convert to decimal")
    print("3. Binary counting")
    print("4. Quit")

    while True:  # Loop until the user enters a valid choice
        # Get the user's choice
        choice = input("\nWhat would you like to do [1,2,3,4]? ")

        # Check if choice is a valid integer between 1 and 4
        valid_choice = True  # Assume the user entered a valid choice
        for char in choice:  # Loop through each character in the choice
            if char not in "0123456789":  # If the character is not a digit
                valid_choice = False  # Set the valid_choice flag to False
                # Display an error message if the user inputs an alphanumeric value
                print("Please make sure your number contains digits 0-9 only.")

        if valid_choice:  # If the user entered a valid choice of integer
            if int(choice) in range(1, 5):  # If the user entered a valid choice of integer between 1 and 4
                return int(choice)  # Return the user's choice
            else:  # If the user entered an invalid choice of integer
                # Display an error message
                print("Invalid choice. Please enter either 1, 2, 3 or 4.")


def convert_to_binary(decimal_number):  # Convert a decimal number to binary

    binary = ''  # Initialize the binary string

    while decimal_number > 0:  # Loop until the decimal number is 0
        quotient = decimal_number // 2  # Get the quotient
        remainder = decimal_number % 2  # Get the remainder
        # Add the remainder to the binary string
        binary = str(remainder) + binary
        decimal_number = quotient  # Set the decimal number to the quotient

    return binary  # Return the binary string


def convert_to_decimal(binary_number):  # Convert a binary number to decimal

    decimal = 0  # Initialize the decimal number
    power = 0   # Initialize the power

    while binary_number > 0:  # Loop until the binary number is 0
        # Add the decimal value of the binary digit to the decimal number
        decimal += (binary_number % 10) * (2 ** power)
        binary_number //= 10  # Get the next binary digit
        power += 1  # Increment the power
    return decimal  # Return the decimal number


# Display the binary counting from 1 to the decimal number entered by the user
def binary_counting(decimal_number):
    print('')

    # Loop from 1 to the decimal number entered by the user
    for i in range(1, decimal_number+1):
        # Convert the decimal number to binary
        binary_number = convert_to_binary(i)
        # Display the decimal number and the binary number
        print(f"Decimal: {i} = binary: {binary_number}")


# Check if the number entered by the user is a binary number
def check_if_binary(binary_number):
    binary_digits = '01'  # Initialize the binary digits
    is_binary = True  # Initialize the is_binary flag
    index = 0  # Initialize the index

    # Loop until the is_binary flag is False or the index is less than the length of the binary number
    while is_binary and index < len(binary_number):
        # If the binary digit is not in the binary digits
        if binary_number[index] not in binary_digits:
            is_binary = False  # Set the is_binary flag to False
        index += 1  # Increment the index

    if is_binary:  # If the is_binary flag is True
        return True
    else:
        return False


def is_integer(input_str):  # Check if the number entered by the user is an integer
    try:  # Try to convert the input string to an integer
        int(input_str)  # Convert the input string to an integer
        return True
    except ValueError:  # If the input string cannot be converted to an integer
        return False


def main():  # Main function

    display_details()  # Display the program details

    flag = True  # Initialize the flag

    while flag:  # Loop until the flag is False
        choice = get_menu_choice()  # Get the user's choice

        if choice == 1:
            valid_input = False  # Initialize the valid_input flag

            while not valid_input:  # Loop until the valid_input flag is True
                # Get input from the user
                decimal_number = input("\nPlease enter number: ")

                if is_integer(decimal_number):  # If the input is an integer
                    binary_number = convert_to_binary(
                        int(decimal_number))  # Convert the input to binary
                    # Display the binary number
                    print(f'\nBinary number: {binary_number}')
                    valid_input = True  # Set the valid_input flag to True
                else:
                    # Display an error message
                    print("Please make sure your number contains digits 0-9 only.")

        elif choice == 2:
            valid_input = False  # Initialize the valid_input flag

            while not valid_input:  # Loop until the valid_input flag is True
                # Get input from the user
                binary_number = input("\nPlease enter binary number: ")
                if check_if_binary(binary_number):  # If the input is a binary number
                    decimal_number = convert_to_decimal(
                        int(binary_number))  # Convert the input to decimal
                    # Display the decimal number
                    print(f'\nDecimal number: {decimal_number}')
                    valid_input = True  # Set the valid_input flag to True
                else:
                    # Display an error message
                    print("Please make sure your number contains digits 0-1 only.")

        elif choice == 3:
            valid_input = False  # Initialize the valid_input flag

            while not valid_input:  # Loop until the valid_input flag is True
                # Get input from the user
                decimal_number = input("\nPlease enter number: ")
                if is_integer(decimal_number):  # If the input is an integer
                    # Display the binary counting
                    binary_counting(int(decimal_number))
                    valid_input = True  # Set the valid_input flag to True
                else:
                    # Display an error message
                    print("Please make sure your number contains digits 0-9 only.")

        elif choice == 4:
            print("\nGoodbye.")  # Display a goodbye message
            flag = False  # Set the flag to False


if __name__ == "__main__":  # If this is the main module
    main()  # Call the main function
