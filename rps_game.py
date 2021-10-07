import random

turns = ["rock", "paper", "scissors"]
computer_score = 0
human_score = 0
games_played = 0

while True:
    games_played +=1
    computer_turn = random.choice(turns)

    while True:
        human_turn = input("Enter human turn: ").lower()
        if human_turn == "rock" or human_turn == "paper" or human_turn == "scissors":
            break
        elif human_turn == "stop":
            exit()
        else:
            print("Select only from rock, paper or scissors")

    print(f"Computer: {computer_turn} VS. Human: {human_turn}")

    if computer_turn == human_turn:
        print(f"Draw! Score: {computer_score}:{human_score}")

    elif ((computer_turn == "paper" and human_turn == "rock") or 
            (computer_turn == "scissors" and human_turn == "paper") or 
            (computer_turn == "rock" and human_turn == "scissors")):
        computer_score += 1
        print(f"Computer wins! Score: {computer_score}:{human_score}")

    else:
        human_score += 1
        print(f"Human wins! Score: {computer_score}:{human_score}")
