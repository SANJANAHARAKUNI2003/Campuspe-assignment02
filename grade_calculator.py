try:
    
    print("----------------")
    print("Grade Calculator")
    print("----------------")

    # Create empty list to store marks of 5 subjects
    marks = []

    # Variable to store total marks
    total = 0

    # Counter variable to track subject number
    i = 1

    # Loop runs 5 times to take input for 5 subjects
    while i <= 5:

        # Ask user to enter marks for current subject
        mark_input = input("Enter marks for subject " + str(i) + " (out of 100) : ")

        # Check if input is empty
        if mark_input == "":
            print("Marks cannot be empty")
            continue   # restart loop without increasing i

        # Convert input to integer
        # This will raise error if user enters text
        mark = int(mark_input)

        # Check if marks are within valid range (0 to 100)
        if mark < 0 or mark > 100:
            print("Marks must be between 0 to 100")
            continue   # ask again for same subject

        # Store valid mark in list
        marks.append(mark)

        # Add mark to total
        total = total + mark

        # Move to next subject
        i = i + 1

    # Percentage = total marks divided by number of subjects
    percentage = total / 5


    # Assign grade based on percentage range
    if percentage >= 90:
        grade = "A+ (Outstanding)"

    elif percentage >= 80:
        grade = "A (Excellent)"

    elif percentage >= 70:
        grade = "B (Good)"

    elif percentage >= 60:
        grade = "C (Average)"

    elif percentage >= 50:
        grade = "D (Pass)"

    else:
        grade = "F (Fail)"


    # Student must score at least 40 in every subject to pass
    pass_status = "Pass"

    # Counter to check each subject mark
    j = 0

    # Loop through marks list
    while j < 5:

        # If any subject has less than 40, student fails
        if marks[j] < 40:
            pass_status = "Fail"
            break   # exit loop early

        j = j + 1


    print("\nMarks in each subject :")

    # Display marks subject-wise
    k = 0
    while k < 5:
        print("Subject", k+1, ":", marks[k])
        k = k + 1

    # Display total marks
    print("\nTotal Marks :", total, "/ 500")

    # Display percentage
    print("Percentage :", percentage, "%")

    # Display grade
    print("Grade :", grade)

    # Display pass/fail result
    print("Result :", pass_status)


# This handles invalid input like letters instead of numbers
except:
    print("Invalid input :( Please enter integer marks only")
