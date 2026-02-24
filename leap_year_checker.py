print("---- Leap Year Checker ------")

try:
    # input() returns a string
    year_input = input("Enter a year : ")

    # Check if input is empty
    if year_input == "":
        print("Year cannot be empty")

    else:
        # Convert input string to integer
        # This will raise error if user enters text
        year = int(year_input)

        # Year must be greater than 0
        # There is no year 0 or negative year 
        if year <= 0:
            print("Year must be greater than 0")

        else:

            # Check leap year condition
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):

                print("\nYear:", year)
                print("Result: Leap Year")

                # If divisible by 400, it is always leap year
                if year % 400 == 0:
                    print("Reason: Divisible by 400")

                # If divisible by 4 but not by 100, it is leap year
                elif year % 100 != 0:
                    print("Reason: Divisible by 4 and NOT divisible by 100")

            else:
                # If condition fails, it is not leap year
                print("\nYear:", year)
                print("Result: NOT a Leap Year")

                # Explain reason

                # Not divisible by 4 then not leap year
                if year % 4 != 0:
                    print("Reason: Not divisible by 4")

                # Divisible by 100 but not 400 then not leap year
                elif year % 100 == 0 and year % 400 != 0:
                    print("Reason: Divisible by 100 but NOT divisible by 400")

# Handle invalid input like letters or symbols
except:
    print("Invalid input :( Please enter numeric year only.")
