# Nicholas Constantine
# CS125 - Python Scripting
# 10/27/21

# define variables
list = []
userInput = 0
maximum = 0
minimum = 0

# ask for user input
userInput = input("Enter a number: ")
list.append(float(userInput))
while userInput != "done": 
    userInput = input("Enter another number: ")
    try: 
        list.append(float(userInput))
    except: 
        if userInput == "done":
            break
        print("Invalid input")
    
# calculate max and min values
maximum = str(max(list))
minimum = str(min(list))
print()
print("Minimum: " + minimum)
print("Maximum: " + maximum)
