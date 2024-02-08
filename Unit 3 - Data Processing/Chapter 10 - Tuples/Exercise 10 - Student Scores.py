# Nicholas Constantine
# CS125 - Python Scrypting
# 11/12/21

# creating the dictionary and variables
userInput = ""
students = dict()
score = 0

# ask for user input (for dictionary)
while userInput != "done":
    userInput = input("What is the student's name? ")
    if userInput == "done":
        break
    else:
        score = float(input("What is their score? "))
        students[userInput] = score
        print("")

# sorts dictionary
print()
print("=== Student Scores ===")
tuple = list(students.items())
tuple.sort()
for key,val in tuple:
    print(key, val)
    
# prompt for student name and display score
print()
name = input("Display score for: ")
for key,val in tuple:
    if key == name:
        print("Score: " + str(val))
print()
