from replit import clear

from art import glogo
auction_over = False
print(glogo)

bids = {}


def find_highest_bidder(bidding_record):
  top_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > top_bid:
      top_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${top_bid}.")

while auction_over == False:
  name = input("Enter your name: ")
  price = int(input("Enter your bid: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
  if should_continue == "no":
    auction_over= True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
