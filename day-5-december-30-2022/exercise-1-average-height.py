# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

count = 0
heights_added = 0
for i in student_heights:
    count += 1
    heights_added += i
print(round(heights_added/count))
