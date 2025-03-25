import random

user_win = 0
prog_win = 0
tie = 0
options = ['r','p','s']

while True:
    user_input = input("Type R: Rock/ P: Paper/ S:Scissors or Q to quit: ").lower()
    if (user_input == "q"):
        break
    if user_input not in options:
        print("Enter the valid input!!")
        continue

    random_number= random.randint(0,2)
    #rock :0 , paper: 1 , scissors: 2

    prog_input = options[random_number]
    if (prog_input == user_input):
        tie = tie+1
        print("Its a tie")
    else:
        if(user_input == options[0]):
            if(prog_input == options[1]):
                print("Computer Wins!")
                prog_win = prog_win+1
            else:
                print("User Wins!")
                user_win = user_win+1
        elif(user_input == options[1]):
            if(prog_input == options[0]):
                print("User Wins!")
                user_win = user_win+1
            else:
                print("Computer Wins!")
                prog_win = prog_win+1
        else:
            if(prog_input == options[0]):
                print("Computer Wins!")
                prog_win = prog_win+1
            else:
                print("User Wins!")
                user_win = user_win+1

print("No of times Computer won:" + str(prog_win))
print("No of times User won:" + str(user_win))
print("No of times game ties:" + str(tie))