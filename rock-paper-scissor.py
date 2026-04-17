def rock_paper_scissor_protocol (move: str) -> str:
    if move == "rock":
        return "paper"
    elif move == "paper":
        return "scissor"
    elif move == "scissor":
        return "rock"

    else:
        move=input("rock or paper or scissor? ")
        print(rock_paper_scissor_protocol(move))
        
def proceed_protocol (ans: str) -> str:
    if ans == "yes":
        umove=input("what's your move? (rock/paper/scissor) ")
        print(rock_paper_scissor_protocol(umove))
    elif ans == "no":
        print("ok :(")
    else:
        ans=input("yes or no? ")
        proceed_protocol(ans)

ua=input("do you wanna play rock,paper,scissor? (yes/no) ")
proceed_protocol(ua)