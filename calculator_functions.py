
# Function for addition
# Takes two numbers as input and returns their sum
def add(a, b):
    result = a + b   # add both numbers
    return result    # return the result back to where function was called


# Function for subtraction
# Returns difference between first and second number
def subtract(a, b):
    result = a - b   # subtract b from a
    return result


# Function for multiplication
# Returns product of two numbers
def multiply(a, b):
    result = a * b   # multiply both numbers
    return result


# Function for division
# Handles division and checks division by zero error
def divide(a, b):
    # Division by zero is mathematically undefined
    if b == 0:
        return "Division by zero is not allowed"
    else:
        result = a / b
        return result


# Function for modulus
# Modulus returns the remainder after division
def modulus(a, b):
    # Modulus by zero is not allowed
    if b == 0:
        return "Modulus by zero is not allowed"
    else:
        result = a % b
        return result


# Function for power
# Returns power of  two numbers
def power(a, b):
    result = a ** b  
    return result




# This function controls the calculator menu and user interaction
def calculator():

    # Infinite loop to keep calculator running until user exits
    while True:

        # Display calculator menu options
        print("\nCalculator Menu")
        print("------------------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        try:
            # Ask user to choose an operation
            choice_input = input("Enter your choice (1-7): ")

            # Check if input is empty
            if choice_input == "":
                print("Choice cannot be empty")
                continue   # restart loop

            # Convert choice into integer
            choice = int(choice_input)

            # Exit condition
            if choice == 7:
                print("Exiting calculator...")
                break   # exit loop and stop calculator

            # Check if choice is valid (between 1 and 7)
            if choice < 1 or choice > 7:
                print("Invalid choice (choose between 1 to 7)")
                continue

            # Ask user to enter two numbers
            num1_input = input("Enter first number : ")
            num2_input = input("Enter second number : ")

            # Check if numbers are empty
            if num1_input == "" or num2_input == "":
                print("Numbers cannot be empty")
                continue

            # Convert inputs into float (to allow decimal values)
            num1 = float(num1_input)
            num2 = float(num2_input)

            

            # Call correct function based on user choice using if-elif

            if choice == 1:
                result = add(num1, num2)
                print("Result :", result)

            elif choice == 2:
                result = subtract(num1, num2)
                print("Result :", result)

            elif choice == 3:
                result = multiply(num1, num2)
                print("Result :", result)

            elif choice == 4:
                result = divide(num1, num2)
                print("Result :", result)

            elif choice == 5:
                result = modulus(num1, num2)
                print("Result :", result)

            elif choice == 6:
                # Convert power to integer because loop requires whole number
                result = power(num1, int(num2))
                print("Result :", result)

        except:
            # Handles invalid inputs like letters or symbols
            print("Invalid input :( Please enter numbers only")




# Call calculator function to start the program
calculator()
