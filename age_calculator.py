try:
    # Store the current year in a variable.
    # This is used to calculate the person's age.
    current_year = 2026

    # Ask the user to enter their birth year.
    # input() returns a string, so we convert it to integer using int()
    birth_year = int(input("Enter your birth year : "))

    # Validate that the birth year is positive.
    # A birth year cannot be 0 or negative.
    if birth_year <= 0:
        raise ValueError("Birth year must be positive.")
    
    # Validate that the birth year is not in the future.
    # Someone cannot be born after the current year.
    if birth_year > current_year:
        raise ValueError("Birth year cannot be in the future")

    # Calculate current age by subtracting birth year from current year.
    age = current_year - birth_year

    # Convert age into different units for more detailed information.

    # Age in months (1 year = 12 months)
    age_months = age * 12

    # Age in days (approximation: 1 year = 365 days)
    age_days = age * 365

    # Age in hours (1 day = 24 hours)
    age_hours = age_days * 24

    # Age in minutes (1 hour = 60 minutes)
    age_minutes = age_hours * 60

    # Calculate how many years left until the person turns 100
    years_to_100 = 100 - age

    # Calculate the exact year when the person will turn 100
    years_when_100 = birth_year + 100

    # Display all calculated age details in a readable format
    print("\n----------- Age Details ------------")
    print("Current Age  :", age, "years")
    print("Age in months  :", age_months, "months")
    print("Age in Days  :", age_days, "days")
    print("Age in Hours  :", age_hours, "hours")
    print("Age in Minutes  :", age_minutes, "minutes")

    # Check if the person is less than 100 years old
    if years_to_100 > 0:
        print("Years until age 100 :", years_to_100,
              "years from now (that is in the year",
              years_when_100, "your age will be 100)")
    else:
        # If age is already 100 or more
        print("You are already 100 or older")

# This block handles errors caused by invalid input
# such as entering text instead of numbers or invalid birth year
except ValueError as e:
    print("Invalid input!", e)

# This block handles any unexpected errors that were not predicted
except Exception:
    print("Something went wrong. Please try again :(")
