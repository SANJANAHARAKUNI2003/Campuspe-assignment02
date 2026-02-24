# 1. Factorial Function
# Factorial of n = n × (n-1) × (n-2) × ... × 1
def factorial(n):

    # Factorial is not defined for negative numbers
    if n < 0:
        return "Factorial not defined for negative numbers"

    # Initialize result as 1 (neutral element of multiplication)
    result = 1

    # Start loop from 1 to n
    i = 1

    # Multiply all numbers from 1 to n
    while i <= n:
        result = result * i
        i = i + 1

    return result


# 2. Prime Check Function
# Prime number has exactly 2 factors: 1 and itself
def is_prime(n):

    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Start checking from 2 up to n-1
    i = 2

    while i < n:

        # If divisible by any number, not prime
        if n % i == 0:
            return False

        i = i + 1

    # If no divisor found, number is prime
    return True


# 3. Fibonacci Function
def fibonacci(n):

    # Negative input is invalid
    if n < 0:
        return "Invalid input"

    # First Fibonacci number
    elif n == 0:
        return 0

    # Second Fibonacci number
    elif n == 1:
        return 1

    # Initialize first two numbers
    a = 0
    b = 1

    # Counter starts from 2
    count = 2

    # Calculate Fibonacci using loop
    while count <= n:

        # Next number = sum of previous two numbers
        c = a + b

        # Shift values forward
        a = b
        b = c

        count = count + 1

    return b


# 4. Sum of Digits Function
def sum_of_digits(n):

    # Convert negative number to positive
    if n < 0:
        n = -n

    total = 0

    # Extract each digit and add
    while n > 0:

        digit = n % 10      # get last digit
        total = total + digit
        n = n // 10         # remove last digit

    return total


# 5. Reverse Number Function
def reverse_number(n):

    # Track if number was negative
    negative = False

    if n < 0:
        negative = True
        n = -n

    reverse = 0

    # Extract digits and build reverse number
    while n > 0:

        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    # Restore negative sign if needed
    if negative == True:
        reverse = -reverse

    return reverse


# 6. Armstrong Number Function
def is_armstrong(n):

    if n < 0:
        return False

    original = n
    total = 0
    count = 0

    temp = n

    # Count number of digits
    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = n

    # Calculate sum of digits raised to power of count
    while temp > 0:

        digit = temp % 10

        power = 1
        i = 0

        # Calculate digit^count manually
        while i < count:
            power = power * digit
            i = i + 1

        total = total + power

        temp = temp // 10

    # Check if equal to original number
    if total == original:
        return True
    else:
        return False


# 7. GCD Function (Greatest Common Divisor)
# Using here Euclidean Algorithm
def gcd(a, b):

    # Convert to positive numbers
    if a < 0:
        a = -a

    if b < 0:
        b = -b

    # Repeat until remainder becomes 0
    while b != 0:

        temp = b
        b = a % b
        a = temp

    return a


# 8. LCM Function (Least Common Multiple)
def lcm(a, b):

    if a == 0 or b == 0:
        return 0

    gcd_value = gcd(a, b)

    result = (a * b) // gcd_value

    # Ensure positive result
    if result < 0:
        result = -result

    return result


# 9. Perfect Number Function
def is_perfect_number(n):

    if n <= 0:
        return False

    total = 0
    i = 1

    # Add all factors except number itself
    while i < n:

        if n % i == 0:
            total = total + i

        i = i + 1

    if total == n:
        return True
    else:
        return False


# 10. Menu Function (Main Control)
def math_menu():

    # Infinite loop until user exits
    while True:

        # Display menu options
        print("\nNUMBER SYSTEM MENU")
        print("------------------")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        try:

            # Take user choice
            choice_input = input("Enter your choice (btw 1-10): ")

            # Check empty input
            if choice_input == "":
                print("Choice cannot be empty")
                continue

            choice = int(choice_input)

            # Exit condition
            if choice == 10:
                print("Exiting program...")
                break


            # Functions requiring one number
            if choice >= 1 and choice <= 6 or choice == 9:

                num_input = input("Enter a number : ")

                if num_input == "":
                    print("Input cannot be empty")
                    continue

                num = int(num_input)

                # Call appropriate function
                if choice == 1:
                    print("Factorial :", factorial(num))

                elif choice == 2:
                    if is_prime(num):
                        print("Prime number")
                    else:
                        print("Not a prime number")

                elif choice == 3:
                    print("Fibonacci :", fibonacci(num))

                elif choice == 4:
                    print("Sum of digits :", sum_of_digits(num))

                elif choice == 5:
                    print("Reversed number :", reverse_number(num))

                elif choice == 6:
                    if is_armstrong(num):
                        print("Armstrong number")
                    else:
                        print("Not an Armstrong number")

                elif choice == 9:
                    if is_perfect_number(num):
                        print("Perfect number")
                    else:
                        print("Not a perfect number")


            # Functions requiring two numbers
            elif choice == 7 or choice == 8:

                a_input = input("Enter first number : ")
                b_input = input("Enter second number : ")

                if a_input == "" or b_input == "":
                    print("Inputs cannot be empty")
                    continue

                a = int(a_input)
                b = int(b_input)

                if choice == 7:
                    print("GCD :", gcd(a, b))

                elif choice == 8:
                    print("LCM :", lcm(a, b))

            else:
                print("Invalid choice")

        except:
            print("Invalid input")


# Program starts here
math_menu()
