# Nicholas Constantine
# CS 125 – Python Scripting
# 8/21/21

print("Nicholas Constantine") #display name

#Conversion calculations
stones = float(input("Enter the weight in stones: "))
pounds = round(stones * 14, 2)
ounces = round(pounds * 16, 2)
kilograms = round(pounds / 2.2, 2)


# Display results
print("======================================================")
print(str(stones) + " stones is:")
print(str(pounds) + " pounds")
print(str(ounces) + " ounces")
print(str(kilograms) + " kilograms")
