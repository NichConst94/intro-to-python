# Nicholas Constantine
# CS125 - Python Scripting
# 8/29/2021

# declare variables
hours = 0
excessHours = 0
rate = 0
gross = 0

# ask for input and output
hours = float(input("How many hours did you work this pay period? "))
rate = float(input("What is your current pay rate? "))

# OT calculations
if hours > 40 : #OT pay
    excessHours = hours - 40
    gross = round((40 * rate) + (excessHours * (1.5 * rate)), 2)
    gross = "{:.2f}".format(gross)
    print("Your gross pay this pay period is $" + str(gross) + " with OT pay")
else : # No OT pay
    gross = round(rate * hours, 2)
    gross = "{:.2f}".format(gross)
    print("Your gross pay this pay period is $" + str(gross))
