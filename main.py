from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
print("My Rock, Paper and Scissor Game!!")
score=0
C=0

while C<5:

    player = input("What's your move?  :")
    if player == computer:
        print("Tie!")
        print(score)
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            score=score - 1
            print(score)
        else:
            print("You win!", player, "smashes", computer)
            score = score + 1
            print(score)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            score = score - 1
            print(score)
        else:
            print("You win!", player, "covers", computer)
            score = score + 1
            print(score)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            score = score - 1
            print(score)
        else:
            print("You win!", player, "cut", computer)
            score = score + 1
            print(score)
    else:
        print("That's not a valid play. Check your spelling!")
    C = C + 1

print('Your final score is: ' +str(score))