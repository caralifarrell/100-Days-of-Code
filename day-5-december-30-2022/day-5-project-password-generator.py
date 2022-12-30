#Password Generator Project

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

randomised_letters = random.choices(letters, k = nr_letters)
randomised_symbols = random.choices(symbols, k = nr_symbols)
randomised_numbers = random.choices(numbers, k = nr_numbers)

generated_password = randomised_letters + randomised_symbols + randomised_numbers
ordered = ''.join(generated_password)
print(f"Your non-randomized password (not recommended) is: {ordered}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random

generated_password_randomised = randomised_letters + randomised_symbols + randomised_numbers
random.shuffle(generated_password_randomised)
shuffled = ''.join(generated_password_randomised)
print(f"The randomized version of your password is: {shuffled}")
