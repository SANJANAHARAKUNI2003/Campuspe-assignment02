#using try and except block 
try:
    sentence = input("Enter a sentence :").strip()

    if len(sentence) == 0: #if user enters empty input
       raise ValueError("Empty input")
    
    if sentence.isdigit(): #if user enters only numeric value 
        raise ValueError("Numeric input not allowed")
    
    words = sentence.split() #breaks string wherever space is found and stores each word as a list element

# if users enters nothing will end up getting index error so to avoid that will use if- else condition

    print(" Original : ", sentence)  # priniting original sentence

    print(" Total Characters (with spaces) : " , len(sentence)) #Total characters with spaces(prints total number of characters including spaces ) using len()

    print(" Total Characters (without spaces) : " , len(sentence.replace(" ", ""))) #Total Characters without spaces(prints total number of characters excluding spaces) using replace(" ","")

    print(" Total Words : ", len(words)) #Total words(counts total number of words in sentence) first breaks the sentence into list of words and then counts the list items

    print(" UPPERCASE : ", sentence.upper()) # UPPER Case(prints all the characters in upper case) using upper()

    print(" lowercase : ", sentence.lower()) # lower case(prints all the characters in lower case) using lower()

    print(" Title Case : ", sentence.title()) # Title case(first character of every word is capitalized) using title()

    print(" First word : ", words[0] ) #First word(prints  only first word of sentence) first word is always at index 0 after splitting 

    print(" Last word : ", words[-1] ) #Last word(prints  only last word of sentence) last word is always at index -1 after splitting 
    
    print(" Reversed : ", sentence[::-1]) #reversed sentence(uses slicing)
except ValueError:
    print("Invalid input :( Please enter proper sentence")
 
    

    




