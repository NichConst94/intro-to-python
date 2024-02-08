# Nicholas Constantine
# CS125 - Python Scripting
# 10/13/21

# defining the function
def charCount(string, letter):
    count = 0
    length = len(string) - 1
    index = 0
    while index <= length:
        if string[index] == letter:
            count = count + 1
        index = index + 1
    print(count)
    
# user input ant output
userString = input("Enter a word or phrase: ")
userLetter = input("Enter a letter: ")
charCount(userString, userLetter)
