import random
from game_data import data
from art import logo
from art import vs

choice_a=""
choice_b=""
def play_game():
    score=0
    correct=True
    choice_a=random.choice(data)

    choice_b=random.choice(data)


    while correct:


        choice_a_follower=choice_a["follower_count"]
        choice_b_follower=choice_b["follower_count"]
        print(logo)
        print(f"compare A: {choice_a['name']} , a {choice_a['description']} from {choice_a['country']}")
        print(vs)
        print(f"against B: {choice_b['name']} , a {choice_b['description']} from {choice_b['country']}")
        correct=True

        option=input("guess who has more followers:'a' or 'b'")
        print("\n"*20)
        if option=="a" and choice_a_follower>choice_b_follower:
            score+=1
            print(f"you are right! current score={score}")
            choice_a=choice_b
            choice_b=random.choice(data)
        elif option=="b" and choice_b_follower>choice_b_follower:
            score+=1
            print(f"you are right! current score={score}")
            choice_a = choice_b
            choice_b = random.choice(data)
        elif option=="a" and choice_a_follower<choice_b_follower:
            correct=False
            print(f"sorry thats wrong your final score:{score}")
        elif option=="b" and choice_b_follower<choice_a_follower:
            correct=False
            print(f"sorry thats wrong your final score:{score}")
play=True
while play:
    again=input("do you still want to play 'yes' or 'no' ")
    if again=="yes":
        play=True
        play_game()
    else:
        play=False