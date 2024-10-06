# 1 = stone 
# 0 = scissor
# -1 = paperm
import random
def error():
    raise ValueError("Your Gave Invalid option.")
def check (user,computer):
    if user == 1 and computer == 0:
        print("User won")
    elif user == 1 and computer == -1:
        print("Computer won")
    elif user == 0 and computer == 1:
        print("Computer won")
    elif user == 0 and computer == -1:
        print("Computer won")
    
    elif user==-1 and computer == 1:
        print("User won")
    elif user == -1 and computer == 0:
        print("Computer won")
    elif user < -1 or user > 1:
        error()
    else:
        print("No Winner")
for i in range(0,5):
        user=int(input("Enter your choice (1 for stone , 0 for scissors ,-1 for paper = )"))
        computer = random.randint(-1,1)
        print(user)
        print(computer)
        check(user,computer)
