# Nicholas Constantine
# CS125 - Python Scripting
# 10/5/21

# Declare variables
sum = 0
numCount = 0
average = 0
number = 0

# Loop code and user input
userInput = input("Enter a number: ")
while userInput != "done":
    try: 
        sum = sum + float(userInput)
        numCount = numCount + 1
    except:
        print("Invalid input")
    userInput = input("Enter another number: ")

# Print results
average = sum / numCount
print("")
print("Sum: " + str(sum))
print("Average: " + str(average))
print("Count: " + str(numCount))
