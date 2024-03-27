import random # Reuse existing import to generate random numbers

# Check for a winner
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"] # Define options for rock, paper, scissors game.

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
     # Get user input and convert to lowercase for consistency. If the user types 'q', break out of the loop
    if user_input == "q":
        break
    
    if user_input not in ["rock", "paper", "scissors"]:# Check for invalid input
        continue

    # Get computer's random choice
    random_number = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2 = scissors
    computer_pick = options[random_number]

    print("\nYou picked ", user_input, "and the computer picked", computer_pick)

# Determine winner
    if (user_input == "rock" and computer_pick == "scissors"):
        print("YOU WON!")
        user_wins += 1
    

    elif (user_input == "paper" and computer_pick == "rock"):
        print("YOU WON!")
        user_wins += 1
    

    elif (user_input == "scissors" and computer_pick == "paper"):
        print("YOU WON!")
        user_wins += 1

    else:
        print("You Lost!")
        computer_wins += 1
    
# Print final results  
print("You Won", user_wins, "times.")
print("Computer Won", computer_wins, "times.")
print("Goodbye!!!")
