# Exercise 2
name = input("Enter your name: ")
print("Hello " + name + ". Welcome to python!")
print("================================================")

#Exercise 3
hoursWorked = int(input("Enter hours worked this pay period: "))
payRate = int(input("Enter your pay rate: "))
pay = str(hoursWorked * payRate)
print("Gross pay: $" + pay)
print("================================================")

#Exercise 5
celcius = int(input("Enter the temperature in celcius: "))
fahrenheit = (celcius * (9/5)) + 32
print(str(celcius) + " degrees C is " + str(fahrenheit) + " degrees F")
