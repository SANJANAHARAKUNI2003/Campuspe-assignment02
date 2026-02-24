try:

    print("Number Pattern Printer")
    print("----------------------")

    # Display available pattern choices to user
    print("Choose a pattern:")
    print("1 - Increasing Number Triangle")
    print("2 - Repeating Number Triangle")
    print("3 - Inverted Decreasing Number Triangle")
    print("4 - Palindromic Number Triangle")
    print("5 - Floyd's Triangle")                     # creative pattern 1
    print("6 - Right-Aligned Increasing Triangle")   #  creative pattern 2
    print("7 - Diamond Number Pattern")              # creative pattern 3


    pattern_input = input("Enter pattern number ( btw 1 to 7 only) : ")

    # Check if input is empty
    if pattern_input == "":
        print("Pattern number cannot be empty")

    else:
        pattern = int(pattern_input)  # convert string to integer

        # Validate pattern range
        if pattern < 1 or pattern > 7:
            print("Please choose pattern btw 1 to 7")

        else:

            #height input
            height_input = input("Enter height : ")

            # Check empty height input
            if height_input == "":
                print("Height cannot be empty")

            else:
                height = int(height_input)

                # Height validation
                if height <= 0:
                    print("Height should be greater than 0")

                elif height > 30:
                    print("Height must be btw 1 to 30")

                else:

                    print("\nOutput Pattern:\n")

                    if pattern == 1:

                        i = 1  # row counter

                        while i <= height:

                            j = 1  # column counter

                            # print numbers from 1 to current row number
                            while j <= i:
                                print(j, end=" ")
                                j = j + 1

                            print()  # move to next line
                            i = i + 1


                    elif pattern == 2:

                        i = 1

                        while i <= height:

                            j = 1

                            # print same number equal to row number
                            while j <= i:
                                print(i, end=" ")
                                j = j + 1

                            print()
                            i = i + 1


                    elif pattern == 3:

                        i = height

                        while i >= 1:

                            j = i

                            while j >= 1:
                                print(j, end=" ")
                                j = j - 1

                            print()
                            i = i - 1


                    elif pattern == 4:

                        i = 1

                        while i <= height:

                            # print spaces for alignment
                            spaces = height - i
                            while spaces > 0:
                                print(" ", end="")
                                spaces = spaces - 1

                            # print increasing numbers
                            j = 1
                            while j <= i:
                                print(j, end="")
                                j = j + 1

                            # print decreasing numbers
                            j = i - 1
                            while j >= 1:
                                print(j, end="")
                                j = j - 1

                            print()
                            i = i + 1


                    elif pattern == 5:

                        i = 1
                        num = 1  # number counter

                        while i <= height:

                            j = 1

                            while j <= i:
                                print(num, end=" ")
                                num = num + 1
                                j = j + 1

                            print()
                            i = i + 1


                    elif pattern == 6:

                        i = 1

                        while i <= height:

                            spaces = height - i

                            while spaces > 0:
                                print(" ", end=" ")
                                spaces = spaces - 1

                            j = 1

                            while j <= i:
                                print(j, end=" ")
                                j = j + 1

                            print()
                            i = i + 1


                    elif pattern == 7:

                        # Upper part
                        i = 1

                        while i <= height:

                            spaces = height - i
                            while spaces > 0:
                                print(" ", end="")
                                spaces = spaces - 1

                            j = 1
                            while j <= i:
                                print(j, end="")
                                j = j + 1

                            j = i - 1
                            while j >= 1:
                                print(j, end="")
                                j = j - 1

                            print()
                            i = i + 1

                        # Lower part
                        i = height - 1

                        while i >= 1:

                            spaces = height - i
                            while spaces > 0:
                                print(" ", end="")
                                spaces = spaces - 1

                            j = 1
                            while j <= i:
                                print(j, end="")
                                j = j + 1

                            j = i - 1
                            while j >= 1:
                                print(j, end="")
                                j = j - 1

                            print()
                            i = i - 1

# catches invalid input like letters instead of numbers
except:
    print("Invalid input :( Please enter numbers only")
