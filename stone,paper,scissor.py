import random
user_score = 0
computer_score = 0
lst = ["Stone","Paper","Scissor"]
print("Welcome to my Stone, Paper And Scissor Game XX")
print("*"*50)
user_choice = input("Do you play game??")
while user_choice == "Y" or user_choice == 'y':
    user_turn = input("Please Choose one of Stone, Paper and Scissor------->>>>")
    computer_turn = random.choice(lst)
    print("Choice of user:: ",user_turn)
    print("Choice of computer:: ",computer_turn)
    if user_turn == "Stone" or user_turn == "stone":
        if computer_turn=="Stone":
            print("It's tie.")
        elif computer_turn=="Paper":
            computer_score+=1
            print("You loss. Computer is winner. Better luck for next time.")
        else:
            user_score+=1
            print("You win.Great Achievement.")
    elif user_turn == "Paper" or user_turn == "paper":
        if computer_turn == "Paper":
            print("It's tie.")
        elif computer_turn=="Scissor":
            computer_score+=1
            print("You loss.Computer is winner. Better luck for next time.")
        else:
            user_score+=1
            print("You win.Great Achievement.")
    else:
        if computer_turn == "Scissor":
            print("It's tie.")
        elif computer_turn == "Stone":
            computer_score+=1
            print("You loss.Computer is winner. Better luck for next time.")
        else:
            user_score+=1
            print("You win.Great Achievement.")

    print("Do you play game again???")
    user_choice = input("Y/N--->>>")

print("X"*50)
print("Computer's Score == ",computer_score)
print("User's Score == ",user_score)
if computer_score > user_score:
    print("Sorry!!!!!!!!,Computer win.")
elif computer_score < user_score:
    print("User win.")
else:
    print("Tie game.")