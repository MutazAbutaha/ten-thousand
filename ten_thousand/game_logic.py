import random
class GameLogic :
    @staticmethod
    def roll_dice(num_dice=6):
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
        # Calculate the score for a six-of-a-kind
        if 6 in dice_counts:
            value = dice_counts.index(6) + 1
            if value == 1:
                score += 1800
            elif value == 5:
                score += 900
            else:
                score += value * 200
        return score
    
    # Call the function
    
if __name__ == "__main__":
    game = GameLogic()
    roll_dice = game.roll_dice()
    print(game.calculate_score(roll_dice))
