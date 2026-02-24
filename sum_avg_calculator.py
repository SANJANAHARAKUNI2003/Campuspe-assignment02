try:
    print("Sum and Average Calculator")
    print("--------------------------")

    count_input = input("How many numbers? ")

    # check empty input
    if count_input == "":
        print(" Count cannot be empty")

    else:
        count = int(count_input)

        # check invalid count
        if count <= 0:
            print("Error: Count must be greater than 0")

        elif count > 100:
            print(" Too many numbers. Please enter count up to 100")

        else:
            total_sum = 0
            i = 1

            # take first number separately to initialize max and min
            first_input = input("Enter number 1: ")

            if first_input == "":
                print(" Number cannot be empty")

            else:
                first_number = int(first_input)

                total_sum = first_number
                maximum = first_number
                minimum = first_number

                i = 2

                # loop for remaining numbers
                while i <= count:

                    number_input = input("Enter number " + str(i) + ": ")

                    # check empty
                    if number_input == "":
                        print(" Empty input entered")
                        break

                    number = int(number_input)

                    # add to sum
                    total_sum = total_sum + number

                    # check maximum
                    if number > maximum:
                        maximum = number

                    # check minimum
                    if number < minimum:
                        minimum = number

                    i = i + 1

                # calculate average only if all inputs were entered
                if i > count:

                    average = total_sum / count

                    print("\nResults")
                    print("----------")
                    print("Sum :", total_sum)
                    print("Average :", average)
                    print("Maximum :", maximum)
                    print("Minimum :", minimum)

except:
    print(" Invalid input:( Please enter integer values only")
