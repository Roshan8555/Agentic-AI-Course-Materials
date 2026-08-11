#1) Rock paper Scissors game
#2) Story generator (random.choice()) [when,what,how,who,where -->
#3) Otp generate to email

#Use Random module --> Rock,paper,scissor

import random
player1 = input('Enter the choice:-->Rock,Paper,scissors:').lower()
player2 = random.choice(['Rock','Paper','Scissors']).lower()
print("Player2 Selection:",player2)

if player1 == player2:
    print("It's a Tie!")

elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

else:
    print("Invalid Choice! Please enter Rock, Paper, or Scissors.")
