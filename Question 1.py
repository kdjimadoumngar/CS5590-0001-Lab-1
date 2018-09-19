# 1. search in a string and find the first non-repeated characters in that string
# Input: Deep data structure
# Output: p
# (hint: if there is space in the string you need to consider the whole as one string. In the above example Deepdatastructure)

# The function to return index of first non-returning character


string = "Deepdatastructure" # The input string

while string !="": # While loop to loop through the string
    string_length0 = len(string) # Determine the length of the string
    char = string[0]    # Exrtractiong the first char of the string
    string = string.replace(char, "")
    string_length1 = len(string)
    if string_length1 == string_length0-1:
            print (char)
            break;
else:
    print("No answer") # Else print no answer




