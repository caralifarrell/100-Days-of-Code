#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

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
