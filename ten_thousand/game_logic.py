import random
class GameLogic :
    @staticmethod
    def roll_dice(num_dice = 6):
        """
        Rolls the six dice.
        Parameters:
        num_dice (int): The number of dice to roll.
        Returns:
        tuple: A tuple containing the values of the six dice rolled.
        """
        dice_values = []
        for i in range(num_dice):
            dice_values.append(random.randint(1, 6))
        return tuple(dice_values)
    @staticmethod
    def calculate_score(dice):
        """
        Calculates the score for a roll of Dice10000.
        Parameters:
        dice (tuple): A tuple containing the values of the six dice rolled.
        Returns:
        int: The total score for the roll.
        """
        score = 0
        dice_counts = [dice.count(i) for i in range(1, 7)]
        # Calculate the score for ones, fives, and three-of-a-kind
        for value, count in enumerate(dice_counts, 1):
            if count >= 3:
                if value == 1:
                    score += 1000
                else:
                    score += value * 100
                count -= 3
            if value == 1:
                score += count * 100
            elif value == 5:
                score += count * 50
        # Calculate the score for four-of-a-kind
        for value, count in enumerate(dice_counts, 1):
            if count >= 4:
                if value == 5:
                    score += value * 100 - 50
                elif value == 1:
                    score += 900
                else :
                    score += value * 100
        # Calculate the score for a straight
        if all(dice_counts[i] == 1 for i in range(6)):
            score += 1350
        # Calculate the score for three pairs
        if dice_counts.count(2) == 3:
            score += 1500
        # Calculate the score for a five-of-a-kind
        if 5 in dice_counts:
            value = dice_counts.index(5) + 1
            if value == 1:
                score += 900
            elif value == 5:
                score += 450
            else:
                score += value * 100
        if 6 in dice_counts:
            value = dice_counts.index(6) + 1
            if value == 1:
                score += 1800
            elif value == 5:
                score += 900
            else:
                score += value * 200
        return score
    @staticmethod
    def play_game():
        total_score = 0
        round_number = 1
        dice_remaining = 6
        all_dice_scored_rounds = 0
        points = 0
        final_points = 0
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input (">")
        if response.lower() == "y" or response.lower() == "yes":
            while True  :
                check = 0
                if response.lower() == "y" or response.lower() == "yes" or dice_remaining == 6:
                    print(f"Starting round {round_number}")
                print(f"Rolling {dice_remaining} dice...")
                dice = list(GameLogic.roll_dice(dice_remaining))
                dice_output = "*** "
                for num in dice:
                    dice_output += f"{num} "
                dice_output += "***"
                print(dice_output)
                points = GameLogic.calculate_score(dice)
                if  round_number>20:
                    print(f"Thanks for playing. You earned {total_score} points")
                    break
                while True:
                    if points == 0:
                        print('''**************************************
** Zilch! No points for this round. **
**************************************''')
                        check = 1
                        round_number += 1
                        dice_remaining = 6
                        total_score -= final_points
                        final_points = 0
                        print(f"You banked {final_points} points in round {round_number}")
                        print(f"Total score is {total_score} points")
                        break
                    if check == 1 :
                        break
                    print("Enter dice to keep, or (q)uit:")
                    response = input(">")

                    if response.lower() == "q" or response.lower() == "quit" or response.lower() == "b":
                        
                        break
                    dice_to_keep = []
                    invalid_input = False
                    removed_dices = dice[:]
                    for value in response:
                        if value in map(str, dice):
                            dice.remove(int(value))
                        elif value not in map(str, dice) or response == '' :
                            print(f"Cheater!!! Or possibly made a typo...  Please try again.")
                            dice = removed_dices
                            print("***", " ".join(str(num) for num in dice), "***")
                            invalid_input = True
                            break
                        dice_to_keep.append(int(value))
                    if invalid_input:
                        continue
                    k = len(GameLogic.get_scorers(dice_to_keep))
                    dice_remaining -= k
                    points = GameLogic.calculate_score(dice_to_keep)
                    final_points += points
                    print(f"You have {final_points} unbanked points and {dice_remaining} dice remaining")
                    break
                if check == 0:

                    if response.lower() == "q" or response.lower() == "quit":
                        print(f"Thanks for playing. You earned {total_score} points")
                        break
                    if dice_remaining == 0:
                        dice_remaining = 6
                        all_dice_scored_rounds += 1
                        if all_dice_scored_rounds >= 3:
                            all_dice_scored_rounds = 0
                    if all_dice_scored_rounds > 2:
                        print("You have scored all dice for 3 consecutive rounds. Starting a new game.")
                        break
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    response = input (">")
                    if response.lower() == "r" or response.lower() == "roll":
                        total_score += points
                        continue
                    elif response.lower() == "b" or response.lower() == "bank":
                        total_score += points
                        print(f"You banked {final_points} points in round {round_number}")
                        print(f"Total score is {total_score} points")
                        round_number += 1
                        final_points = 0
                        dice_remaining = 6
                    elif response.lower() == "q" or response.lower() == "quit":
                        print(f"Thanks for playing. You earned {total_score} points")
                        break
        else:
            print("OK. Maybe another time")
    @staticmethod
    def validate_keepers(roll, keepers):
        roll, keepers = list(roll), list(keepers)
        for value in keepers:
            if value in roll:
                roll.remove(value)
            elif value not in roll:
                return False
        return True
    @staticmethod
    def get_scorers(dice):
        all_dice_score = GameLogic.calculate_score(dice)
        if all_dice_score == 0 :
            return tuple()
        scorers = []
        for i,value  in enumerate(dice):
            sub_roll = dice[:i] + dice[i+1:]
            sub_score = GameLogic.calculate_score(sub_roll)
            if sub_score != all_dice_score :
                scorers.append(value)
        return tuple(scorers)
if __name__ == "__main__":
    game = GameLogic()
    game.play_game(10)