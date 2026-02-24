# Multiplication Table Generator
# This program asks user for a number and range, then prints multiplication table

try:
    print("Multiplication Table Generator")
    print("------------------------------")

    # input number
    number_input = input("Enter number: ")

    # check empty input
    if number_input == "":
        print(" Number cannot be empty")

    else:
        number = int(number_input)

        # input range
        range_input = input("Enter range (end): ")

        # check empty range
        if range_input == "":
            print(" Range cannot be empty")

        else:
            end = int(range_input)

            # validate range
            if end <= 0:
                print(" Range must be greater than 0")

            elif end > 50:
                print(" Range too large. Please enter range between 1 and 50")

            else:
                print("\nMultiplication Table of", number)
                print("-----------------------------")

                i = 1

                # loop to generate table
                while i <= end:

                    result = number * i

                    print(number, "x", i, "=", result)

                    i = i + 1


except:
    print(" Invalid input :( Please enter integer values only.")