try:
    print("Palindrome Checker")
    print("------------------")

    # Take input from user (can be word or number)
    user_input = input("Enter word/number : ")

    # Check if input is empty
    if user_input == "":
        print("Input cannot be empty")

    else:
        # Store original input for display and comparison
        original = user_input

        # Convert input to lowercase to ignore case sensitivity
        # Example: Mom and mom should be treated same
        lower_input = ""
        i = 0

        # Using built-in lower() function to convert entire string to lowercase
        lower_input = original.lower()

        # Create empty string to store reversed result
        reversed_input = ""

        # Start index from last character of string
        # len(original) gives total length, so last index is length - 1
        index = len(original) - 1

        # Display heading for step-by-step reverse process
        print("\nStep-by-step reversing :")

        # Loop runs until index reaches first character
        while index >= 0:

            # Show which character is being added
            print("Adding :", original[index])

            # Add character to reversed string
            reversed_input = reversed_input + original[index]

            # Move to previous character
            index = index - 1


        # Convert reversed string to lowercase for comparison
        reversed_lower = reversed_input.lower()


        print("\nOriginal :", original)
        print("Reversed:", reversed_input)


        # Compare original lowercase and reversed lowercase
        # If same  palindrome
        if lower_input == reversed_lower:
            print("Result : PALINDROME")

        # Otherwise not palindrome
        else:
            print("Result : NOT A PALINDROME")


# Handles invalid input errors
except:
    print("Invalid input :(")
