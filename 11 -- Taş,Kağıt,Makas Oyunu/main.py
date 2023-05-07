

"""
Taş,Kağıt,Makas oyunu.
Oyuncu seçim yaptıktan sonra bilgisayar da seçim yapıyor ve karşılaştırılıyor.Oyun , oyuncu "q" 'ya basana kadar devam ediyor.
"""

import random


print(("-"*20) + " Rock,Paper,Scissors " + ("-"*20))
print("press 'q' to exit\n")

actions=["rock","paper","scissors"]

computer_score=0
player_score=0


while True:

    player_choice=input("Your choice : ")
    computer_choice=random.choice(actions)

    if player_choice == "rock":
        if computer_choice == "rock":
            print("Computer's choice:",computer_choice,"\nScoreless!")
        elif computer_choice == "paper":
            print("Computer's choice:",computer_choice,"\nYou lose!")
            computer_score += 100
        elif computer_choice == "scissors":
            print("Computer's choice:",computer_choice,"\nYou win!")
            player_score += 100


    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Computer's choice:",computer_choice,"\nYou win!")
            player_score += 100
        elif computer_choice == "paper":
            print("Computer's choice:",computer_choice,"\nScoreless!")
        elif computer_choice == "scissors":
            print("Computer's choice:",computer_choice,"\nYou lose!")
            computer_score += 100


    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("Computer's choice:",computer_choice,"\nYou lose!")
            computer_score += 100
        elif computer_choice == "paper":
            print("Computer's choice:",computer_choice,"\nYou win!")
            player_score += 100
        elif computer_choice == "scissors":
            print("Computer's choice:",computer_choice,"\nScoreless!")

    else :
        if player_choice == "q" :
            print("Exit..")
            break



if player_score == computer_score :
    print("\nThere is no winner . Player's score ({}) : Computer's score ({})".format(player_score,computer_score))
elif player_score > computer_score :
    print("\nPlayer is winner . Player's score ({}) : Computer's score ({})".format(player_score,computer_score))
elif player_score < computer_score :
    print("\nComputer is winner . Player's score ({}) : Computer's score ({})".format(player_score,computer_score))




"""
Output:

-------------------- Rock,Paper,Scissors --------------------
press 'q' to exit

Your choice : paper
Computer's choice: rock
You win!
Your choice : rock
Computer's choice: paper
You lose!
Your choice : scissors
Computer's choice: scissors
Scoreless!
Your choice : rock
Computer's choice: paper
You lose!
Your choice : paper
Computer's choice: rock
You win!
Your choice : scissors
Computer's choice: scissors
Scoreless!
Your choice : q
Exit..

There is no winner . Player's score (200) : Computer's score (200)
"""