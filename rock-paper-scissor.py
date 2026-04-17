import random
# need to set the game properly

def counter_move (move: str)-> str:
# create to avoid doing all situations
    if move == "rock":
        return "paper"
    elif move == "paper":
        return "scissor"
    else:
        return "rock"

def play_stage (playermove: str, computermove: str) -> str:
# need a proper game rule
    if playermove == computermove:
        print("Tie")
    elif playermove == counter_move(computermove):
        print ("You win!")
    else: 
        print ("You lost...")

def input_valve () -> str:
# gauge the player typed input
    while True:
        move=input("Choose rock, paper, or scissor: ").lower()
        if move in ["rock", "paper", "scissor"]:
            return move
        print("Invalid choice. Try again")

def main():
# play the game
    print(" Welcome back to RPS!")
    while True:
        pmove=input_valve()
        cmove=random.choice(["rock", "paper", "scissor"])
        print(f"Computer chose: {cmove}")
        play_stage(pmove, cmove)

        again=input("Wanna play again? (y/n): ")
        if again != "y":
            print("Thanks for playing!")
            break

while True:
    q1=input("Wanna play r-p-scissor? (y/n): ").lower()
    if q1 == "y":
        main()
        break
    break