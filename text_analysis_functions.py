# Function to count number of words in text
def count_words(text):

    count = 0          # stores number of words
    in_word = False    # flag to check if currently inside a word
    i = 0              # index variable

    # Loop through each character in text
    while i < len(text):

        # If character is not space and we are NOT already in a word
        if text[i] != " " and in_word == False:
            count = count + 1    # new word found so increase count
            in_word = True       # now we are inside a word

        # If character is space then word ended
        elif text[i] == " ":
            in_word = False      # reset flag

        i = i + 1

    return count


# Function to count vowels
def count_vowels(text):

    count = 0
    vowels = "aeiouAEIOU"   # string containing all vowels

    i = 0
    while i < len(text):

        j = 0

        # Compare current character with each vowel
        while j < len(vowels):

            if text[i] == vowels[j]:
                count = count + 1   # vowel found
                break               # stop checking further vowels

            j = j + 1

        i = i + 1

    return count


# Function to count consonants
def count_consonants(text):

    count = 0
    vowels = "aeiouAEIOU"

    i = 0
    while i < len(text):

        ch = text[i]

        # Check if character is alphabet
        if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):

            is_vowel = False
            j = 0

            # Check if alphabet is vowel
            while j < len(vowels):

                if ch == vowels[j]:
                    is_vowel = True
                    break

                j = j + 1

            # If alphabet and NOT vowel then consonant
            if is_vowel == False:
                count = count + 1

        i = i + 1

    return count


# Function to reverse text manually
def reverse_text(text):

    reversed_text = ""
    i = len(text) - 1   # start from last character

    # Loop backwards
    while i >= 0:
        reversed_text = reversed_text + text[i]
        i = i - 1

    return reversed_text


# Function to check palindrome
def is_palindrome(text):

    reversed_text = reverse_text(text)

    # Convert both to lowercase for case-insensitive comparison
    text_lower = text.lower()
    reversed_lower = reversed_text.lower()

    # Compare original and reversed text
    if text_lower == reversed_lower:
        return True
    else:
        return False


# Function to remove vowels from text
def remove_vowels(text):

    result = ""
    vowels = "aeiouAEIOU"

    i = 0
    while i < len(text):

        ch = text[i]
        is_vowel = False

        j = 0
        while j < len(vowels):

            if ch == vowels[j]:
                is_vowel = True
                break

            j = j + 1

        # If not vowel then add to result
        if is_vowel == False:
            result = result + ch

        i = i + 1

    return result


# Function to count frequency of each word
def word_frequency(text):

    freq = {}     # dictionary to store word counts
    word = ""     # temporary word storage
    i = 0

    # Loop until end of text
    while i <= len(text):

        # If character is not space then build word
        if i < len(text) and text[i] != " ":
            word = word + text[i]

        else:
            # Word completed
            if word != "":

                word_lower = word.lower()

                # Update dictionary count
                if word_lower in freq:
                    freq[word_lower] = freq[word_lower] + 1
                else:
                    freq[word_lower] = 1

                word = ""   # reset for next word

        i = i + 1

    return freq


# Function to find longest word
def longest_word(text):

    longest = ""
    word = ""
    i = 0

    while i <= len(text):

        # Build word character by character
        if i < len(text) and text[i] != " ":
            word = word + text[i]

        else:

            # Compare lengths
            if len(word) > len(longest):
                longest = word

            word = ""

        i = i + 1

    return longest


# Main analysis function
def analyze_text(text):

    print("\n=== TEXT ANALYSIS ===")

    # Call all functions
    words = count_words(text)
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    reversed_text_value = reverse_text(text)
    palindrome = is_palindrome(text)
    no_vowels = remove_vowels(text)
    longest = longest_word(text)
    freq = word_frequency(text)

    # Display results
    print("Words :", words)
    print("Vowels :", vowels)
    print("Consonants :", consonants)
    print("Reversed :", reversed_text_value)

    if palindrome == True:
        print("Palindrome : Yes")
    else:
        print("Palindrome : No")

    print("Without vowels :", no_vowels)
    print("Longest word :", longest, "(" + str(len(longest)) + " letters )")

    print("Word Frequency :")
    for key in freq:
        print(key + ":", freq[key])


# Main program
try:

    print("Text Analysis Program")
    print("---------------------")

    # Take input from user
    text = input("Enter text : ")

    # Check empty input
    if text == "":
        print("Text cannot be empty")

    else:
        analyze_text(text)

except:
    print("Invalid input :(")
