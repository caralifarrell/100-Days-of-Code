from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

def highest_bidder(bidding_list):
  highest_bid = 0
  winner = ""
  for bidder in bidding_list:
    bid_amount = bidding_list[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
    
  
more_bidding = True

while more_bidding:
  bids = {}
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if more_bidders == "yes":
    clear()
  elif more_bidders == "no":
    more_bidding = False
    highest_bidder(bids)
