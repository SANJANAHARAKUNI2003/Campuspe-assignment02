try:
    print("Factorial Calculator")
    print("--------------------")

    # Take input from the user
    # input() always returns a string
    number_input = input("Enter a number : ")

    # Check if user entered nothing (empty input)
    if number_input == "":
        print("Input cannot be empty")

    else:
        # Convert string input to integer
        # This will raise error if user enters text like "abc"
        number = int(number_input)

        # Factorial is not defined for negative numbers
        if number < 0:
            print("Factorial is not defined for negative numbers")

        # Special case: factorial of 0 is always 1
        elif number == 0:
            print("0! = 1")

        else:
            # Initialize factorial result as 1
            # because factorial is multiplication and 1 is neutral element
            factorial = 1

            # Start loop from the number down to 1
            i = number

            # Print the beginning of factorial expression
            print(str(number) + "! = ", end="")

            # Loop runs until i becomes 1
            while i >= 1:

                # Multiply current value with factorial
                factorial = factorial * i

                # Print current number in sequence
                print(i, end="")

                # Print multiplication symbol except after last number
                if i > 1:
                    print(" × ", end="")

                # Decrease value of i by 1 each iteration
                i = i - 1

            # Finally print the calculated factorial result
            print(" = " + str(factorial))

# This block handles invalid input such as letters or decimal numbers
except:
    print("Invalid input :( Please enter integer values only")
