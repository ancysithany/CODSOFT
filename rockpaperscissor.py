import random

def winner(user, computer):
    if user == computer:
        return "Both have same guess,I see.That's a tie!!"
    elif (user == 'rock' and computer== 'scissors') or \
         (user== 'scissors' and computer == 'paper') or \
         (user== 'paper' and computer == 'rock'):
        return "YAY!!You win!"
    else:
        return "UH-OH!!Computer wins!"

def game():
    print("Lets Start!!")
    user_score = 0
    computer_score = 0

    while True:
        user= input("Choose rock, paper, or scissors or 'quit' to end the game): ").lower()
        if user== 'quit':
            break
        elif user not in ['rock', 'paper', 'scissors']:
            print("Invalid choice.Choose between rock, paper, or scissors.")
            continue

        computer= random.choice(['rock', 'paper', 'scissors'])

        print("You chose:", user)
        print("Computer chose:", computer)

        result = winner(user, computer)
        print(result)

        if result == "YAY!!You win!":
            user_score += 1
        elif result == "UH-OH!!Computer wins!":
            computer_score += 1

        print("Your score:", user_score)
        print("Computer's score:", computer_score)

    print("Thanks foe playing bud!! See you again!")

if __name__ == "__main__":
    game()
