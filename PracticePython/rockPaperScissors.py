quit = False
while not quit:
    user1_input = input("user1 input")
    user2_input = input("user2 input")
    if user1_input == "rock" and user2_input == "scissor" or user1_input == "scissor" and user2_input == "paper" or user1_input == "paper" and user2_input == "rock":
        print("user1 wins!") 
    elif user2_input == "rock" and user1_input == "scissor" or user2_input == "scissor" and user1_input == "paper" or user2_input == "paper" and user1_input == "rock":
        print("user2 wins!")
    else:
        print("Draw")
    replay = input("Do you want to play again?")
    if replay == "N":
        quit = True
