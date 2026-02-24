# Loop runs until user enters a valid bill amount
while True:
    try:
        # Ask user to enter total bill amount
        bill_amnt_input = input("Enter total bill amount: ")

        # Check if input is empty
        # Empty input is not valid, so ask again
        if bill_amnt_input == "":
            print("Bill amount cannot be empty. Please enter a value")
            continue  # restart loop

        # Convert input string to float (because bill can have decimals)
        total_bill = float(bill_amnt_input)

        # Bill amount must be greater than zero
        if total_bill <= 0:
            print("Bill amount cannot be negative or zero")
            continue

        # If everything is valid, exit loop
        break

    except:
        # This handles invalid inputs like letters or symbols
        print("Invalid input :( Please enter numeric value")


# Loop runs until user enters valid number of people
while True:
    try:
        # Ask user to enter number of people
        people_input = input("Enter number of people: ")

        # Check if input is empty
        if people_input == "":
            print("Number of people cannot be empty")
            continue

        # Convert input to integer (people count must be whole number)
        people = int(people_input)

        # Number of people must be greater than zero
        if people <= 0:
            print("Number of people must be greater than zero")
            continue

        # Exit loop if valid
        break

    except:
        # Handle invalid input like text or decimal numbers
        print("Invalid input. Please enter a whole number")


# Loop runs until valid tax percentage is entered
while True:
    try:
        # Ask user to enter tax percentage
        tax_input = input("Enter tax percentage (Enter 0 if no tax): ")

        # Check empty input
        if tax_input == "":
            print("Tax percentage cannot be empty. Enter 0 if no tax")
            continue

        # Convert to float because percentage can be decimal
        tax_percent = float(tax_input)

        # Tax cannot be negative
        if tax_percent < 0:
            print("Tax percentage cannot be negative. Enter 0 if no tax")
            continue

        # Exit loop if valid
        break

    except:
        print("Invalid input. Please enter a numeric value")


# Loop runs until valid tip percentage is entered
while True:
    try:
        # Ask user to enter tip percentage
        tip_input = input("Enter tip percentage (Enter 0 if no tip): ")

        # Check empty input
        if tip_input == "":
            print("Tip percentage cannot be empty. Enter 0 if no tip")
            continue

        # Convert to float
        tip_percent = float(tip_input)

        # Tip cannot be negative
        if tip_percent < 0:
            print("Tip percentage cannot be negative")
            continue

        # Exit loop if valid
        break

    except:
        print("Invalid input. Please enter a numeric value") 

sub_total = total_bill
tax_amount = (sub_total * tax_percent) / 100 
after_tax = sub_total + tax_amount
tip_amount = (after_tax * tip_percent) / 100 
total = after_tax + tip_amount
per_person = total / people

print("\n---- BILL AMOUNT -----")
print("Subtotal : Rs", round(sub_total, 2))
print("Tax(",tax_input,"%) : Rs", round(tax_amount,2))
print("After tax : Rs", round(after_tax,2))
print("Tip(",tip_input,"%) : Rs", round(tip_amount,2))
print("Total bill : Rs", round(total,2))
print("Amount per person : Rs", round(per_person,2))