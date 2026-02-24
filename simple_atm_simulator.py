try:
    print("ATM SIMULATOR")
    print("-------------")

    # Set initial balance (this acts like money already in account)
    balance = 10000

    # Infinite loop so user can perform multiple operations
    while True:

        # Display ATM menu options
        print("\n--Menu--")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        # Take user choice
        choice_input = input("Enter choice (btw 1-4) : ")

        # Check if input is empty
        if choice_input == "":
            print("Choice cannot be empty")
            continue   # go back to menu

        # Convert input to integer
        choice = int(choice_input)

        if choice == 1:

            # Simply display current balance
            print("Current balance : Rs", balance)


        elif choice == 2:

            # Ask user how much money to deposit
            amount_input = input("Enter amount to deposit : ")

            # Check empty input
            if amount_input == "":
                print("Amount cannot be empty")
                continue

            # Convert input to integer
            amount = int(amount_input)

            # Deposit amount must be positive
            if amount <= 0:
                print("Deposit amount must be greater than 0")
                continue

            # Add deposit amount to balance
            balance = balance + amount

            # Display confirmation
            print("Deposit successful :)")
            print("New balance : Rs", balance)


        elif choice == 3:

            # Ask user how much money to withdraw
            amount_input = input("Enter amount to withdraw : ")

            # Check empty input
            if amount_input == "":
                print("Amount cannot be empty")
                continue

            # Convert input to integer
            amount = int(amount_input)

            # Withdrawal amount must be positive
            if amount <= 0:
                print("Withdrawal amount must be greater than 0")
                continue


            # Check if enough balance is available
            if amount > balance:
                print("Insufficient balance")

            # Maintain minimum balance rule (Rs 500 must remain)
            elif balance - amount < 500:
                print("Minimum balance of Rs.500 must remain")

            else:
                # Subtract withdrawal amount
                balance = balance - amount

                # Display confirmation
                print("Withdrawal successful!")
                print("New balance: Rs", balance)


        elif choice == 4:

            # Exit the loop and program
            print("Thank you for using ATM :)")
            break

        else:
            print("Invalid choice")


# Handles invalid input like letters instead of numbers
except:
    print("Invalid input :( Please enter numbers only.")
