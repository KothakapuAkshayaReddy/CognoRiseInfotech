import random
choice=1
user_score=0
computer_score=0
print("\t\t***Welcome to Rock paper scissor Game***")
print("\n")
while(choice):
    user_choice=int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissor: "))
    if user_choice<0 or user_choice>2:
        print("You entered invalid number, you Lose")
        computer_score+=1
    else:
        computer_choice=random.randint(0,2)
        print("computer chose: ")
        print(computer_choice)
        if computer_choice==user_choice:
            print("It's a tie")
        elif computer_choice==0 and user_choice==2:
            print("You Lose")
            computer_score+=1
        elif user_choice==0 and computer_choice==2:
            print("You Win")
            user_score+=1
        elif computer_choice>user_choice:
            print("You lose")
            computer_score+=1
        elif user_choice>computer_choice:
            print("You Win")
            user_score+=1
    print("Your score is:",user_score)
    print("Computer score is:",computer_score)
    print("If You want to play again enter 1 or else enter 0 :")
    choice=int(input())