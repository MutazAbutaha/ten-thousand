import random
from game_logic import GameLogic
class play(GameLogic):
    def welcome_message(self):
        print("Welcome to Ten Thousand")
        response = input("(y)es to play or (n)o to decline\n> ")
        if response.lower() == "y" or response.lower() == "yes":
            print("Great! Let's start the game.")
            return "OK. Maybe another time"
        elif response.lower() == "n" or response.lower() == "no":
            print("OK. Maybe another time.")
            return "OK. Maybe another time"
        else:
            print("Invalid input. Please try again.")
            return "OK. Maybe another time"
    def play_game(self):
            total_score = 0
            round_number = 1
            dice_remaining = 6
            game_logic = GameLogic()
            print("Welcome to Ten Thousand")
            response = input("(y)es to play or (n)o to decline\n> ")
            if response.lower() == "y" or response.lower() == "yes":
                while True:
                    print(f"Starting round {round_number}")
                    print("Rolling 6 dice...")
                    dice = [random.randint(1, 6) for _ in range(dice_remaining)]
                    print("***", " ".join(str(num) for num in dice), "***")
                    response = input("Enter dice to keep, or (q)uit:\n> ")
                    print(f"You entered: {response}")
                    if response.lower() == "q" or response.lower() == "quit":
                        print(f"Thanks for playing. You earned {total_score} points")
                        return
                    dice = tuple(map(int, response))
                    points = self.calculate_score(dice)
                    print(f"You have {points} unbanked points and {dice_remaining - response.count('5')} dice remaining")
                    response = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
                    if response.lower() == "r" or response.lower() == "roll":
                        dice_remaining = dice_remaining - response.count("5")
                    elif response.lower() == "b" or response.lower() == "bank":
                        total_score += points
                        print(f"You banked {points} points in round {round_number}")
                        print(f"Total score is {total_score} points")
                        round_number += 1
                        dice_remaining = 6
                    elif response.lower() == "q" or response.lower() == "quit":
                        print(f"Thanks for playing. You earned {total_score} points")
                        return
                    else:
                        print("Invalid input. Please try again.")
            else:
                print("OK. Maybe another time")
if __name__ == "__main__":
    game= play()
    game.play_game()