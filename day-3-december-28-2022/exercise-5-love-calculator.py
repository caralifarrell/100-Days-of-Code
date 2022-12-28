# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined = name1 + name2
combined = combined.lower()

count_true = 0
count_love = 0
for i in combined:
    true = ['t','r','u','e']
    for j in true:
        if i == j:
            count_true += 1
    love = ['l','o','v','e']
    for k in love:
        if i == k:
            count_love += 1

score = str(count_true) + str(count_love)
score = int(score)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
