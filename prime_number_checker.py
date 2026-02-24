try:

    
    print("Part 1 : Prime Number Checker")
    print("------------------------------")

    # Take input from user
    number_input = input("Enter a number : ")

    # Check if input is empty
    if number_input == "":
        print("Input cannot be empty")

    else:
        # Convert input string to integer
        number = int(number_input)

        # Negative numbers are not prime
        # Prime numbers exist only for positive integers greater than 1
        if number < 0:
            print(str(number) + " is NOT a prime number (negative numbers are not prime)")

        # 0 and 1 are not prime numbers
        # They do not have exactly two factors
        elif number == 0 or number == 1:
            print(str(number) + " is NOT a prime number")

        # 2 is the smallest and only even prime number
        elif number == 2:
            print("2 is a PRIME number")

        else:
            # Assume number is prime initially
            is_prime = True

            # Start checking from 2 up to number-1
            i = 2

            # Check if number is divisible by any number
            while i < number:

                # If divisible, then not prime
                if number % i == 0:
                    is_prime = False
                    break   # exit loop early

                i = i + 1

            # Display result based on flag
            if is_prime == True:
                print(str(number) + " is a PRIME number")
            else:
                print(str(number) + " is NOT a prime number")


    print("\nPart 2 : Prime Range Finder")
    print("--------------------------------")

    # Take start and end range inputs
    start_input = input("Enter start range : ")
    end_input = input("Enter end range : ")

    # Check if inputs are empty
    if start_input == "" or end_input == "":
        print("Range values cannot be empty")

    else:
        # Convert inputs to integers
        start = int(start_input)
        end = int(end_input)

        # Validate range
        if start > end:
            print("Start range cannot be greater than end range")

        else:
            # Display heading
            print("Prime numbers:", end=" ")

            # Flag to check if any prime found
            found = False

            # Start checking each number in range
            num = start

            while num <= end:

                # Prime numbers start from 2
                if num >= 2:

                    # Assume number is prime
                    is_prime = True

                    # Check divisibility
                    i = 2

                    while i < num:

                        if num % i == 0:
                            is_prime = False
                            break

                        i = i + 1

                    # If prime, print it
                    if is_prime == True:
                        print(num, end=" ")
                        found = True

                # Move to next number
                num = num + 1

            # If no primes found in range
            if found == False:
                print("No prime numbers found in this range")


# Handle invalid input such as letters
except:
    print("Invalid input :( Please enter integer values only")
