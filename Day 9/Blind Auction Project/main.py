from art import logo
print(logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary




def find_the_highest_bider(bider):
    highest_amount=0
    winner=""
    for type in bider:
        bider_amount=bider[type]
        if bider_amount>0:
            highest_amount=bider_amount
            winner=type
    print(f"winner is {winner} with bid of {highest_amount}")


bids={}
new_bids=True
while new_bids:
    new_bids=input("are there any bidders 'yes' or 'no'" )
    if new_bids=="yes":
        new_bids=True
        print("\n"*20)
        name=input("your name")
        bid=int(input("your bid"))
        bids[name]=bid



    else:
          print("\n"*20)
          new_bids=False
          find_the_highest_bider(bids)
