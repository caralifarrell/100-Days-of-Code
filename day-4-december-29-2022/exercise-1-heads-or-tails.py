#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random

#faster way:
#heads_tails = random.choice(['Heads','Tails'])
#print(heads_tails)

heads_tails = random.randint(0,1)
if heads_tails == 0:
    print("Tails")
else:
    print("Heads")
