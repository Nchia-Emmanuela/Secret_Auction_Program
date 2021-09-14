from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print("Welcome to the secret auction program. ")
print(art.logo)

auction_bid = {}
bidding_finished = False

def highest_bidder(record):
  highest_bid = 0
  winner = ""
  for bidder  in record:
    bid_amount = record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"the winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name? : ")
  bid = int(input("What is your bid? $"))
  auction_bid[name] = bid
  other_bidder = input("Are there any other biders? type 'yes' or 'no' : \n")

  if other_bidder == 'no':
    bidding_finished = True
    highest_bidder(auction_bid)
  elif other_bidder == "yes":
    clear()