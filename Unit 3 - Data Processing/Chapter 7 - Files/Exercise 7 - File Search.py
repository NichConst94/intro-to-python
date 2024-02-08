# Nicholas Constantine
# CNIT125 - Python Scripting
# 10/22/21

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

# Ask user for file name and letter
File = open(input("Enter file name: "))
UserLetter = input("Enter a letter: ")

for Line in File:
    charCount(Line, UserLetter)
