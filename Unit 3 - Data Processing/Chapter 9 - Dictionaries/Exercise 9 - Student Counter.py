# Nicholas Constantine
# CS125 - Python Scripting
# 11/1/21

# creating the dictionary and variables
userInput = ""
students = dict()
score = 0

# ask for user input
while userInput != "done":
    userInput = input("What is the student's name? ")
    if userInput == "done":
        break
    else:
        score = float(input("What is their score? "))
        students[userInput] = score
        print("")

# Print length of dictionary
print("")
print("Number of students: " + str(len(students)))
