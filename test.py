# Nicholas Constantine
# CS 125 - Python Scripting

age = 19
print("Hello world! Written in python.")
print("Age: " + str(age))

# Sales tax calculator
print("Enter subtotal: ")
subtotal = float(input())
print("Enter sales tax percentage: ")
salesTax = float(input())
salesTaxAmount = round(salesTax / 100 * subtotal, 2)
totalAmount = round(subtotal + salesTaxAmount, 2)
print("Your total is $" + str(totalAmount) + " with a sales tax of $" + str(salesTaxAmount))
