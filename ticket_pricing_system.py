print("-----Movie Ticket Pricing System -------")

try:
    # AGE INPUT
    age_input = input("Enter age: ")

    if age_input == "":
        print(" Age cannot be empty")

    else:
        age = int(age_input)

        if age <= 0:
            print(" Age cannot be negative or zero")

        else:
            # DAY INPUT
            day = input("Enter day of week: ")

            if day == "":
                print(" Day cannot be empty")

            else:
                # CHECK VALID DAY
                if (day != "Monday" and day != "Tuesday" and day != "Wednesday" and
                    day != "Thursday" and day != "Friday" and day != "Saturday" and
                    day != "Sunday" and day != "monday" and day != "tuesday" and
                    day != "wednesday" and day != "thursday" and day != "friday" and
                    day != "saturday" and day != "sunday"):

                    print(" Invalid day entered (Enter any day btw (Monday-Sunday) or (monday-sunday) only )")

                else:
                    # TICKETS INPUT
                    tickets_input = input("Enter number of tickets: ")

                    if tickets_input == "":
                        print("Error: Number of tickets cannot be empty.")

                    else:
                        tickets = int(tickets_input)

                        if tickets <= 0:
                            print("Error: Number of tickets must be greater than 0.")

                        else:
                            # AGE PRICING
                            if age < 3:
                                base_price = 0
                                category = "Free"

                            elif age <= 12:
                                base_price = 150
                                category = "Child"

                            elif age <= 59:
                                base_price = 300
                                category = "Adult"

                            else:
                                base_price = 200
                                category = "Senior"


                            # DAY DISCOUNT
                            if (day == "Friday" or day == "Saturday" or day == "Sunday" or
                                day == "friday" or day == "saturday" or day == "sunday"):

                                discount = base_price * 20 / 100

                            else:
                                discount = 0


                            final_price = base_price - discount
                            total_amount = final_price * tickets


                            # OUTPUT
                            print("\n=== Ticket Details ===")
                            print("Category:", category)
                            print("Base price:", base_price)
                            print("Discount:", discount)
                            print("Price after discount:", final_price)
                            print("Total amount:", total_amount)

except:
    print("Error: Invalid input. Please enter correct values.")