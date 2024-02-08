# Nicholas Constantine
# CS125 - Python Scripting
# 12/10/2021

# Print welcome message from text file
welcomeFile = open("Welcome message.txt")
welcomeMessage = welcomeFile.read()
print(welcomeMessage)
print()

# asks for veichle year
userInput = input("What year is the car? ")
print()
while True:
    try:
        year = int(userInput)
        userInput = ""
        break
    except:
        userInput = input("What year is the car? ")
        print()

# asks for veichle make
make = input("What make is the car? ")
print()
while True:
    if make == "":
        make = input("What make is the car? ")
        print()
        continue
    else:
        break

# asks for veichle model
model = input("What model is the car? ")
print()
while True:
    if model == "":
        model = input("What model is the car? ")
        print()
        continue
    else:
        break

# asks for car power type for applicable hybrid or electric surcharge (if any)
userInput = userInput = input("Is the veichle a gas, hybrid or electric powered car? ['gas', 'hybrid', 'electric'] ")
print()
while userInput != "gas" and userInput != "hybrid" and userInput != "electric":
    userInput = input("Is the veichle a gas, hybrid or electric powered car? ['gas', 'hybrid', 'electric'] ")
    print()
carPower = userInput
userInput = ""

# creates a dictionary and function to list the sales tax % of all WI counties (sorted by alphabetical order)
# all veichle sales are subject to WI state tax (5%)
# local sales tax is .5% (applies only to certian counties)
countySalesTax = dict()
countySalesTax[1] = 5.5
countySalesTax[2] = 5.5
countySalesTax[3] = 5.5
countySalesTax[4] = 5.5
countySalesTax[5] = 5.5
countySalesTax[6] = 5.5
countySalesTax[7] = 5.5
countySalesTax[8] = 5.5
countySalesTax[9] = 5.5
countySalesTax[10] = 5.5
countySalesTax[11] = 5.5
countySalesTax[12] = 5.5
countySalesTax[13] = 5.5
countySalesTax[14] = 5.5
countySalesTax[15] = 5.5
countySalesTax[16] = 5.5
countySalesTax[17] = 5.5
countySalesTax[18] = 5.5
countySalesTax[19] = 5.5
countySalesTax[20] = 5.5
countySalesTax[21] = 5.5
countySalesTax[22] = 5.5
countySalesTax[23] = 5.5
countySalesTax[24] = 5.5
countySalesTax[25] = 5.5
countySalesTax[26] = 5.5
countySalesTax[27] = 5.5
countySalesTax[28] = 5.5
countySalesTax[29] = 5.5
countySalesTax[30] = 5.5
countySalesTax[31] = 5.5
countySalesTax[32] = 5.5
countySalesTax[33] = 5.5
countySalesTax[34] = 5.5
countySalesTax[35] = 5.5
countySalesTax[36] = 5
countySalesTax[37] = 5.5
countySalesTax[38] = 5.5
countySalesTax[39] = 5.5
countySalesTax[40] = 5.5
countySalesTax[41] = 5.5
countySalesTax[42] = 5.5
countySalesTax[43] = 5.5
countySalesTax[44] = 5.5
countySalesTax[45] = 5.5
countySalesTax[46] = 5.5
countySalesTax[47] = 5.5
countySalesTax[48] = 5.5
countySalesTax[49] = 5.5
countySalesTax[50] = 5.5
countySalesTax[51] = 5.5
countySalesTax[52] = 5
countySalesTax[53] = 5.5
countySalesTax[54] = 5.5
countySalesTax[55] = 5.5
countySalesTax[56] = 5.5
countySalesTax[57] = 5.5
countySalesTax[58] = 5.5
countySalesTax[59] = 5.5
countySalesTax[60] = 5.5
countySalesTax[61] = 5.5
countySalesTax[62] = 5.5
countySalesTax[63] = 5.5
countySalesTax[64] = 5.5
countySalesTax[65] = 5.5
countySalesTax[66] = 5.5
countySalesTax[67] = 5.5
countySalesTax[68] = 5
countySalesTax[69] = 5.5
countySalesTax[70] = 5.5
countySalesTax[71] = 5
countySalesTax[72] = 5.5

# creates a dictionary to pair counties with their number in alphabetical order
countyNum = dict()
countyNum[1] = "Adams"
countyNum[2] = "Ashland"
countyNum[3] = "Barron"
countyNum[4] = "Bayfield"
countyNum[5] = "Brown"
countyNum[6] = "Buffalo"
countyNum[7] = "Burnett"
countyNum[8] = "Calumet"
countyNum[9] = "Chippewa"
countyNum[10] = "Clark"
countyNum[11] = "Columbia"
countyNum[12] = "Crawford"
countyNum[13] = "Dane"
countyNum[14] = "Dodge"
countyNum[15] = "Door"
countyNum[16] = "Douglas"
countyNum[17] = "Dunn"
countyNum[18] = "Eau Claire"
countyNum[19] = "Florence"
countyNum[20] = "Fond du Lac"
countyNum[21] = "Forest"
countyNum[22] = "Grant"
countyNum[23] = "Green"
countyNum[24] = "Green Lake"
countyNum[25] = "Iowa"
countyNum[26] = "Iron"
countyNum[27] = "Jackson"
countyNum[28] = "Jefferson"
countyNum[29] = "Juneau"
countyNum[30] = "Kenosha"
countyNum[31] = "Kewaunee"
countyNum[32] = "La Crosse"
countyNum[33] = "Lafayette"
countyNum[34] = "Langlade"
countyNum[35] = "Lincoln"
countyNum[36] = "Manitowoc"
countyNum[37] = "Marathon"
countyNum[38] = "Marinette"
countyNum[39] = "Marquette"
countyNum[40] = "Menomoniee"
countyNum[41] = "Milwaukee"
countyNum[42] = "Monroe"
countyNum[43] = "Oconto"
countyNum[44] = "Oneida"
countyNum[45] = "Outagamie"
countyNum[46] = "Ozaukee"
countyNum[47] = "Pepin"
countyNum[48] = "Pierce"
countyNum[49] = "Polk"
countyNum[50] = "Portage"
countyNum[51] = "Price"
countyNum[52] = "Racine"
countyNum[53] = "Richland"
countyNum[54] = "Rock"
countyNum[55] = "Rusk"
countyNum[56] = "St. Croix"
countyNum[57] = "Sauk"
countyNum[58] = "Sawyer"
countyNum[59] = "Shawano"
countyNum[60] = "Sheboygan"
countyNum[61] = "Taylor"
countyNum[62] = "Trempealeau"
countyNum[63] = "Vernon"
countyNum[64] = "Vilas"
countyNum[65] = "Walworth"
countyNum[66] = "Washburn"
countyNum[67] = "Washington"
countyNum[68] = "Waukesha"
countyNum[69] = "Waupaca"
countyNum[70] = "Waushara"
countyNum[71] = "Winnebago"
countyNum[72] = "Wood"

# Prints counties by alphabetical order as a function
def listCounties():
    print("1 - Adams")
    print("2 - Ashland")
    print("3 - Barron")
    print("4 - Bayfield")
    print("5 - Brown")
    print("6 - Buffalo")
    print("7 - Burnett")
    print("8 - Calumet")
    print("9 - Chippewa")
    print("10 - Clark")
    print("11 - Columbia")
    print("12 - Crawford")
    print("13 - Dane")
    print("14 - Dodge")
    print("15 - Door")
    print("16 - Douglas")
    print("17 - Dunn")
    print("18 - Eau Claire")
    print("19 - Florence")
    print("20 - Fond du Lac")
    print("21 - Forest")
    print("22 - Grant")
    print("23 - Green")
    print("24 - Green Lake")
    print("25 - Iowa")
    print("26 - Iron")
    print("27 - Jackson")
    print("28 - Jefferson")
    print("29 - Juneau")
    print("30 - Kenosha")
    print("31 - Kewaunee")
    print("32 - La Crosse")
    print("33 - Lafayette")
    print("34 - Langlade")
    print("35 - Lincoln")
    print("36 - Manitowoc")
    print("37 - Marathon")
    print("38 - Marinette")
    print("39 - Marquette")
    print("40 - Menomoniee")
    print("41 - Milwaukee")
    print("42 - Monroe")
    print("43 - Oconto")
    print("44 - Oneida")
    print("45 - Outagamie")
    print("46 - Ozaukee")
    print("47 - Pepin")
    print("48 - Pierce")
    print("49 - Polk")
    print("50 - Portage")
    print("51 - Price")
    print("52 - Racine")
    print("53 - Richland")
    print("54 - Rock")
    print("55 - Rusk")
    print("56 - St. Croix")
    print("57 - Sauk")
    print("58 - Sawyer")
    print("59 - Shawano")
    print("60 - Sheboygan")
    print("61 - Taylor")
    print("62 - Trempealeau")
    print("63 - Vernon")
    print("64 - Vilas")
    print("65 - Walworth")
    print("66 - Washburn")
    print("67 - Washington")
    print("68 - Waukesha")
    print("69 - Waupaca")
    print("70 - Waushara")
    print("71 - Winnebago")
    print("72 - Wood")
    print()
    
# asks user where veichle will be kept and stores tax rate % and name of county
listCounties()
userInput = input("Where will the veichle be kept in? Enter the number that corrosponds to the correct county. Enter 0 to reprint the list.")
while True:
    try:
        if userInput == "0":
            listCounties()
            print()
            userInput = input("Where will the veichle be kept in? Enter the number that corrosponds to the correct county. Enter 0 to reprint the list.")
            continue
        taxRate = float(countySalesTax[int(userInput)])
        county = countyNum[int(userInput)]
        userInput = ""
        print()
        break
    except:
        userInput = input("Where will the veichle be kept in? Enter the number that corrosponds to the correct county. Enter 0 to reprint the list. ")

# prints tax exemptions as a function
def listTaxExemptions():
    print("1 - Motor vehicle previously titled in Wisconsin and purchased from a family member")
    print("2 - Purchaser is Common or Contract Carrier using the vehicle exclusively as such")
    print("3 - Lessor reporting gross receipts from rental or lease")
    print("4 - Purchaser is State of WI or other Federal or WI government unit or agency")
    print("5 - Sales tax already paid to another state")
    print("6 - Purchaser is not a resident of WI and will not use the motor veichle in WI except to remove it from WI")
    print("7 - Purchaser is a WI dealer for a veichle purchased solely for resale")
    print("8 - Religious, charitable, educational, or other nonprofit organization")
    print("9 - Miscellaneous reasons")
    print()

# asks user for any tax exemptions (if any)
listTaxExemptions()
userInput = input("Do any of the above tax exemptions apply to you? If so, enter the correct number that corrosponds to the reason. If not, type 'no'. To reprint the list, enter 0: ")
while True:
    try:
        if userInput == "0":
            print()
            userInput = ""
            listTaxExemptions()
            userInput = input("Do any of the above tax exemptions apply to you? If so, enter the correct number that corrosponds to the reason. If not, type 'no'. To reprint the list, enter 0: ")
            continue
        elif userInput == "no":
            taxExempt = False
            break

        if int(userInput) >= 1 and int(userInput) <= 9:
            userInput = ""
            taxExempt = True
            taxRate = 0
            break
        elif int(userInput) < 0 or int(userInput) > 9:
            print()
            userInput = ""
            userInput = input("Do any of the above tax exemptions apply to you? If so, enter the correct number that corrosponds to the reason. If not, type 'no'. To reprint the list, enter 0: ")
            continue
        else:
            userInput = ""
            break
    except:
        print()
        userInput = ""
        userInput = input("Do any of the above tax exemptions apply to you? If so, enter the correct number that corrosponds to the reason. If not, type 'no'. To reprint the list, enter 0: ")

# asks user for price of the car
print()
userInput = input("What is the price of the car? ")
print()
while True:
    try:
        price = float(userInput)
        price = "{:.2f}".format(price)
        userInput = ""
        break
    except:
        userInput = input("What is the price of the car? ")
        print()

# asks for user's trade-in value
userInput = input("What is your trade-in value? (if any) ")
print()
while True:
    try:
        tradeIn = float(userInput)
        tradeIn = "{:.2f}".format(tradeIn)
        userInput = ""
        break
    except:
        userInput = input("What is your trade-in value? (if any) ")
        print()

# asks for user's down payment
userInput = input("What is your down payment? (if any) ")
print()
while True:
    try:
        downPayment = float(userInput)
        downPayment = "{:.2f}".format(downPayment)
        userInput = ""
        break
    except:
        userInput = input("What is your down payment? (if any) ")
        print()

# calculates net price of the car
netPrice = float(price) - float(tradeIn) - float(downPayment)
netPrice = "{:.2f}".format(netPrice)

# calculates state and local sales tax
if taxExempt == True:
    amountSubjectToTax = 0.00
    amountSubjectToTax = "{:.2f}".format(amountSubjectToTax)
    stateTax = 0.00
    stateTax = "{:.2f}".format(stateTax)
    localTax = 0.00
    localTax = "{:.2f}".format(localTax)
else:
    amountSubjectToTax = netPrice
    stateTax = round(float(netPrice) * 0.05, 2)
    stateTax = "{:.2f}".format(stateTax)

if taxRate == 5:
    localTax = 0.00
    localTax = "{:.2f}".format(localTax)
else:
    localTax = round(float(amountSubjectToTax) * 0.005, 2)
    localTax = "{:.2f}".format(localTax)

# determines if buyer has to pay an annual Electric or Hybrid Vehicle Surcharge
if carPower == "gas":
    surchargeCost = 0.00
elif carPower == "hybrid":
    surcharge = "Hybrid Vehicle Surcharge: $75.00"
    surchargeCost = 75.00
else:
    surcharge = "Electric Vehicle Surcharge: $100.00"
    surchargeCost = 100.00

# prints total cost of purchase and breakdown of fees and taxes
print(str(year) + " " + make + " " + model + " Cost breakdown:")
print("====================================================================================")
print("Title Fee: $164.50")
print("License Plate Fee (Passenger Vehicle): $85.00")
if carPower == "hybrid" or carPower == "electric":
    print(surcharge)
print("Purchase Price: $" + str(price))
print("Less trade-in allowance: $" + str(tradeIn))
print("Less down payment: $" + str(downPayment))
print("Net price: $" + str(netPrice))
print()
print("Taxes and fees:")
print("Amount subject to tax: $" + str(amountSubjectToTax))
print("WI State Tax: $" + str(stateTax))
print(str(county) + " County Tax: $" + str(localTax))

# calculates and prints total cost of registration
print()
totalCost = 164.50 + 85 + float(surchargeCost) + float(netPrice) + float(stateTax) + float(localTax)
totalCost = "{:.2f}".format(totalCost)
print("Cost of registration: $" + totalCost)
