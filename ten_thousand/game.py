
import random
from game_logic import GameLogic

class Play(GameLogic):
    def welcome_message(self):
        pass

    def play_game(self):
        total_score = 0
        round_number = 1
        dice_remaining = 6
        all_dice_scored_rounds = 0
        game_logic = GameLogic()
        print("Welcome to Ten Thousand")
        response = input("(y)es to play or (n)o to decline\n> ")
        if response.lower() == "y" or response.lower() == "yes":
            while True:
                print(f"Starting round {round_number}")
                print("Rolling 6 dice...")
                dice = [random.randint(1, 6) for _ in range(dice_remaining)]
                print("***", " ".join(str(num) for num in dice), "***")

                points = self.calculate_score(dice)
                if points == 0:
                    print('''
                          **************************************
                          ** Zilch! No points for this round. **
                          **************************************
                          ''')
                    round_number += 1
                    dice_remaining = 6
                    continue

                response = input("Enter dice to keep, or (q)uit:\n> ")
                print(f"You entered: {response}")
                if response.lower() == "q" or response.lower() == "quit":
                    print(f"Thanks for playing. You earned {total_score} points")
                    return

                dice_to_keep = []
                invalid_input = False
                for value in response:
                    if value not in map(str, dice):
                        print(f"Invalid input. The dice values are {', '.join(map(str, dice))}. Please try again.")
                        invalid_input = True
                        break
                    dice_to_keep.append(int(value))
                                # Check for invalid input or repeated values
                    response_list = response.split()
                    if  len(set(response_list)) != len(response_list):
                        print(f"Invalid input. The dice values are {', '.join(map(str, dice))}. Please try again.")
                        invalid_input = True
                        break
                

                if invalid_input:
                    continue

                if len(dice_to_keep) > dice_remaining:
                    print(f"You selected more dice than available. Please try again.")
                    continue

                dice_remaining -= len(dice_to_keep)
                points = self.calculate_score(dice_to_keep)
                print(f"You have {points} unbanked points and {dice_remaining} dice remaining")

                if dice_remaining == 0:
                    print("All dice have scored. Rolling 6 new dice...")
                    dice_remaining = 6
                    all_dice_scored_rounds += 1
                    if all_dice_scored_rounds >= 3:
                        print("Hot dice! Rolling 6 new dice...")
                        all_dice_scored_rounds = 0

                if all_dice_scored_rounds > 2:
                    print("You have scored all dice for 3 consecutive rounds. Starting a new game.")
                    total_score = 0
                    round_number = 1
                    dice_remaining = 6
                    all_dice_scored_rounds = 0
                    continue

                response = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
                if response.lower() == "r" or response.lower() == "roll":
                    continue
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
    game = Play()
    game.play_game()
