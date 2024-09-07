import random
from random import randint
from art import logo

easy=0
hard=0
answer = random.randint(0, 100)
def easy_level():
    chances=10
    for _ in range(0,chances):
        number=int(input("guess a number"))
        easy=number
        if easy==answer:
            print("you win")
            print("you have choosed correctly")
            chances=0
            return chances
        elif easy > answer:
            print("number is too high")
            chances-=1
            print(f"you have {chances} attempts left")
            if chances==0:
                print("you lost")
                return chances
        elif easy < answer:
            print("number is too low")
            chances-=1
            print(f"you have {chances} attempts left")
            if chances==0:
                print("you lost")
                return chances


def hard_level():
    chances = 5
    for _ in range(0, chances):
        number = int(input("guess a number"))
        hard = number
        if hard == answer:
            print("you win")
            print("you have choosed correctly")
            chances = 0
            return chances
        elif hard > answer:
            print("number is too high")
            chances -= 1
            print(f"you have {chances} attempts left")
            if chances == 0:
                print("you lost")
                return chances
        elif hard < answer:
            print("number is too low")
            chances -= 1
            print(f"you have {chances} attempts left")
            if chances == 0:
                print("you lost")
                return chances
def play_game():
    print(logo)
    print("welcome to the number guessing game!!")
    print("i am thinking of a number between 1 and 100")


    difficult=input("chose difficulty 'easy' or 'hard' ")
    if difficult=="easy":
        easy_level()
    elif difficult=="hard":
        hard_level()

do=True
while do:
    play=input("do you want to play guess game 'yes' or 'no'")
    if play=="yes":
       play_game()