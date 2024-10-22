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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
list_type = [rock,paper,scissors]
random_list = random.choice(list_type)

if user_choice == 0:
    print(rock)
    print("Computer choose:")
    if random_list == rock:
        print(rock)
        print("It's draw.")
    elif random_list == paper:
        print(paper)
        print("You lose.")
    elif random_list == scissors:
        print(scissors)
        print("You win.")

elif user_choice == 1:
    print(paper)
    print("Computer choose:")
    if random_list == rock:
        print(rock)
        print("You win.")
    elif random_list == paper:
        print(paper)
        print("It's draw.")
    elif random_list == scissors:
        print(scissors)
        print("You lose.")

elif user_choice == 2:
    print(scissors)
    print("Computer choose:")
    if random_list == rock:
        print(rock)
        print("You lose.")
    elif random_list == paper:
        print(paper)
        print("You win.")
    elif random_list == scissors:
        print(scissors)
        print("It's draw.")

else:
    print("Invalid number")