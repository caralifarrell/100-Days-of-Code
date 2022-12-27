# Day 2: Tip Calculator
# December 27, 2022

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_bill = float(total_bill)
tip_percentage = (float(tip_percentage)/100)+1
people = int(people)

result = round((total_bill/people)*tip_percentage,2)
result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")