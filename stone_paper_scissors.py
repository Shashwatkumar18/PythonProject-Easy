import random

rock = ( """

      ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)         
""")

paper = ("""

      PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""

    SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

player_1 = 0

player_1_choice = str(input("Please Choose Any One Of The Three:- "))
player_1_choice = player_1_choice.lower()

if player_1_choice == "rock":
    player_1 = rock
elif player_1_choice == "paper":
    player_1 = paper
elif player_1_choice == "scissors":
    player_1 = scissors

list_game = [rock, paper, scissors]

player_2 = random.choice(list_game)



print("Player 1:- ",player_1)
print("\nPlayer 2:- ",player_2)

if player_1_choice == "rock":
    if player_2 == scissors:
        print("You Won!")
    elif player_2 == paper:
          print("You Loose!")
    elif player_2 == rock:
        print("Match Draw")
elif player_1_choice == "scissors":
    if player_2 == paper:
        print("You Won!")
    elif player_2 == rock:
          print("You Loose!")
    elif player_2 == scissors:
        print("Match Draw")
elif player_1_choice == "paper":
    if player_2 == rock:
         print("You Won!")
    elif player_2 == scissors:
           print("You Loose!")
    elif player_2 == paper:
        print("Match Draw")








