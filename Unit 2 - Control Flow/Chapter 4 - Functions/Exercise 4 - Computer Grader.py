# Nicholas Constantine
# CS 125 - Python Scripting
# 9/27/21

# declare function
def computerGrade(score): 
    if score <= 100 and score >= 90: 
        print("You got an A")
    elif score < 90 and score >= 80: 
        print("You got a B")
    elif score < 80 and score >= 70: 
        print("You got a C")
    elif score < 70 and score >= 60: 
        print("You got a D")
    else: 
        print("You got an F") 

# user input and output
assignmentScore = int(input("What score did you get on the assignment? "))
computerGrade(assignmentScore)
