def find_the_highest(bidder):
    highest_amount=0
    winner=""
    for person in bidder:
        amount=bidder[person]
        if amount>highest_amount:
            highest_amount=amount
            winner=person
    print(f"winner is {winner} with a bid of {highest_amount}")






bids={}
correct_value=True
while correct_value:
    name=input("your name")
    price=int(input("your bid"))
    bids[name]=price
    new_bider=input("type 'yes' for new bidders or type 'no'")
    if new_bider=="yes":
        correct_value=True
    elif new_bider=="no":
        find_the_highest(bids)
