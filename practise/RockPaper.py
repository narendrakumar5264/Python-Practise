import random
item = ["rock" , "paper", " scissors "]
Comp_choise = random.choice(item)  

user_choise = input("Choose rock , paper Or scissors ")
print(f"You  choose: {user_choise}")
print(f"Computer choose: {Comp_choise}")

if user_choise == "rock":
    if Comp_choise == "rock":
        print("Tie! Try Again")
    elif Comp_choise == "paper":
        print("You Lost! Paper covers rock. Try Again")
    elif Comp_choise == "scissors":
        print("You Win! Rock breaks scissors")
elif user_choise == "paper":
    if Comp_choise == "paper":
        print("Tie! Try Again")
    elif Comp_choise == "scissors":
        print("You Lost! Scissors cuts paper. Try Again")
    elif Comp_choise == "rock":
        print("You Win! Paper covers rock")
elif user_choise == "scissors":
    if Comp_choise == "scissors":
        print("Tie! Try Again")
    elif Comp_choise == "rock":
        print("You Lost! Rock breaks scissors. Try Again")
    elif Comp_choise == "paper":
        print("You Win! Scissors cuts paper")


