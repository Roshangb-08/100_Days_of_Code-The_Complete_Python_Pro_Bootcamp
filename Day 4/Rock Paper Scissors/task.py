import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list=[rock,paper,scissors]
ran=input("type 1 for rock, type2 for scissors, type3 for paper")
if ran=='1':
    print(rock)
    computer_choice=random.choice(list)
    print(computer_choice)
    if computer_choice==rock:
        print("draw")
    elif computer_choice==paper:
        print("lose")
    else:
        print("win")
elif ran=='2':
    print(paper)
    computer_choice = random.choice(list)
    print(computer_choice)
    if computer_choice == rock:
        print("win")
    elif computer_choice == paper:
        print("draw")
    else:
        print("lose")
elif ran=='3':
    print(scissors)
    computer_choice = random.choice(list)
    print(computer_choice)
    if computer_choice == rock:
        print("win")
    elif computer_choice == paper:
        print("draw")
    else:
        print("lose")

