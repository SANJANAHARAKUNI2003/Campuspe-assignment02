try:
    print("CALCULATOR")
    print("----------")

    # Take inputs
    num1_input = input("Enter first number : ")
    num2_input = input("Enter second number : ")

    # Check empty input
    if num1_input == "" or num2_input == "":
        print("Input cannot be empty")
        exit()

    num1 = float(num1_input)
    num2 = float(num2_input)

    # Menu
    print("\nChoose operation you want to perform :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == "":
        print("Choice cannot be empty")

    elif choice == '1':
        print("Result =", num1 + num2)

    elif choice == '2':
        print("Result =", num1 - num2)

    elif choice == '3':
        print("Result =", num1 * num2)

    elif choice == '4':
        if num2 == 0:
            print("Oops, cannot divide by zero!")
        else:
            print("Result =", num1 / num2)

    elif choice == '5':
        if num2 == 0:
            print("Oops, cannot perform modulus with zero!")
        else:
            print("Result =", num1 % num2)

    elif choice == '6':
        print("Result =", num1 ** num2)

    else:
        print("Invalid choice :( Please choose between 1 and 6")

except ValueError:
    print("Invalid input :( Please enter numeric values only!")
