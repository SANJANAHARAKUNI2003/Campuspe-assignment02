# Infinite loop so program keeps running until user chooses Exit
while True:

    # Display menu options to user
    print("\n----- Temperature Converter -------")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    try:
        # Take choice input from user
        choice_input = input("Enter your choice (btw 1 to 7 only ) :")

        # Check if input is empty
        if choice_input == "":
            print("Choice cannot be empty.")
            continue   # restart loop and show menu again

        # Convert input to integer
        choice = int(choice_input)

    except:
        # Handle case where input is not a number
        print("Invalid choice :( Enter numbers only")
        continue   # restart loop

    # Exit condition
    if choice == 7:
        print("Exiting ...")
        break   # terminate the loop and program

    # Check if choice is outside valid range
    if choice < 1 or choice > 7:
        print("Invalid choice :( Please select btw 1 to 7)")
        continue

    try:
        # Take temperature value input
        temp_input = input("Enter temperature value  : ")

        # Check empty temperature input
        if temp_input == "":
            print("Temperature cannot be empty")
            continue

        # Convert temperature to float
        temp = float(temp_input)

    except:
        # Handle invalid numeric input
        print("Invalid temperature value. Enter numeric value")
        continue


    # Celsius to Fahrenheit formula: (C × 9/5) + 32
    if choice == 1:
        result = (temp * 9 / 5) + 32
        print("Result:", result, "F")

    # Fahrenheit to Celsius formula: (F − 32) × 5/9
    elif choice == 2:
        result = (temp - 32) * 5 / 9
        print("Result:", result, "C")

    # Celsius to Kelvin formula: C + 273.15
    elif choice == 3:
        result = temp + 273.15

        # Kelvin cannot be negative (scientific rule)
        if result < 0:
            print("Invalid result. Kelvin cannot be negative.")
        else:
            print("Result:", result, "K")

    # Kelvin to Celsius formula: K − 273.15
    elif choice == 4:

        # Input Kelvin cannot be negative
        if temp < 0:
            print("Invalid input. Kelvin cannot be negative.")
        else:
            result = temp - 273.15
            print("Result:", result, "C")

    # Fahrenheit to Kelvin formula: (F − 32) × 5/9 + 273.15
    elif choice == 5:
        result = (temp - 32) * 5 / 9 + 273.15

        # Kelvin cannot be negative
        if result < 0:
            print("Invalid result :( Kelvin cannot be negative")
        else:
            print("Result:", result, "K")

    # Kelvin to Fahrenheit formula: (K − 273.15) × 9/5 + 32
    elif choice == 6:

        # Kelvin cannot be negative
        if temp < 0:
            print("Invalid input :( Kelvin cannot be negative")
        else:
            result = (temp - 273.15) * 9 / 5 + 32
            print("Result:", result, "F")
