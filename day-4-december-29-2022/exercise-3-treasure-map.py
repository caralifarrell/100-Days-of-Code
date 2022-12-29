# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

number = list(str(position))
column = int(number[0])
row = int(number[1])

if column == 1:
    if row == 1:
        row1[0] = ('X')
    if row == 2:
        row2[0] = ('X')
    if row == 3:
        row3[0] = ('X')
elif column == 2:
    if row == 1:
        row1[1] = ('X')
    if row == 2:
        row2[1] = ('X')
    if row == 3:
        row3[1] = ('X')
elif column == 3:
    if row == 1:
        row1[2] = ('X')
    if row == 2:
        row2[2] = ('X')
    if row == 3:
        row3[2] = ('X')

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
