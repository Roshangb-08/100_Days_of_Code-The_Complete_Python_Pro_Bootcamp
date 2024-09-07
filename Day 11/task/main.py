import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def compare(ut,ct):
    if ut>ct and ut<21:
        print(f"your final cards:{user_card}, score:{ut}")
        print(f"computers final cards : {computer_card}, computer score:{ct}")
        print("you win")
    elif ct>ut and ct<21:
        print(f"your final cards:{user_card}, score:{ut}")
        print(f"computers final cards : {computer_card}, computer score:{ct}")
        print("you lose")
    elif ct==ut:
        print(f"your final cards:{user_card}, score:{ut}")
        print(f"computers final cards : {computer_card}, computer score:{ct}")
        print("draw")
def replace(ut,ct):
    if ut>21 and 11 in user_card:
        user_card.remove(11)
        user_card.append(1)
    elif ct>21 and 11 in computer_card:
        computer_card.remove(11)
        computer_card.append(1)
def greater(ut,ct):
    if ut>21:
        print("computer wins")
    elif ct>21:
        print("you win")
    elif ut>21 and ct>21:
        print("both choose higher than 21")

play=input("do you want to play 'y' or 'n'")
if play=="y":
    print("\n"*20)
    print(logo)
    user_card=[]
    computer_card=[]
    for cards in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    user_card_total=sum(user_card)
    computer_card_total=sum(computer_card)
    print(f"your cards:{user_card}, current_score = {user_card_total}")
    print(f"computers first choice: {computer_card[0]}")
    again=True
    while again:
        again_=input("type 'y' to draw another card or 'n'")
        if again_=="y":
            again=True
            user_card.append(deal_card())
            computer_card.append(deal_card())
            user_card_total=sum(user_card)
            computer_card_total=sum(computer_card)
            replace(user_card_total, computer_card_total)
            print(f"your cards:{user_card} , current_score={user_card_total}")
            print(f"computers first choice : {computer_card[0]}")

            if user_card_total>21 or computer_card_total>21:
                again=False
                greater(user_card_total,computer_card_total)
        elif again_=="n":
            again=False
            compare(user_card_total,computer_card_total)




