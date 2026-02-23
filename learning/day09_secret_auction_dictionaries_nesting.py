# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionarym

from art import logo
print (logo)

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bid = {}
should_continue = True
while should_continue:
    name = str(input("What is your name?\n"))
    price = int(input("What is your bid price?\n"))
    bid[name] = price
    restart = input("Is there anyone else who wants to bid? Type 'yes' if there is. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        highest_bidder(bid)
    else:
        print("\n"*100)

