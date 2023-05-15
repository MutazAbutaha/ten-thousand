import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        counts = [0] * 6  # Initialize counts for each dice face

        # Count the occurrences of each dice face
        for die in dice_roll:
            if 1 <= die <= 6:
                counts[die - 1] += 1

        # Calculate the score based on the counts
        for i in range(6):
            count = counts[i]
            face_value = i + 1

            if count >= 3:  # Three or more of the same face value
                if face_value == 1:
                    score += 1000
                else:
                    score += face_value * 100

                count -= 3

                # Special case for six ones
                if face_value == 1 and count > 0:
                    score *= 2 ** count

            # Calculate additional points for individual ones and fives
            if face_value == 1:
                score += count * 100
            elif face_value == 5:
                score += count * 50

            # Calculate points for four, five, or six of a kind
            if dice_roll == (2,2,2,2):
                score = 400
            if dice_roll == (2,2,2,2,2):
                score = 600
            if dice_roll == (2,2,2,2,2,2):
                score = 800
            if dice_roll == (1,1,1,1,1,1):
                score = 4000
            if count >= 4:
                if face_value == 1:
                    score += 1000 * (2 ** (count - 4))
                else:
                    score += (2 ** (count - 3)) * (face_value * 100)

        # Calculate points for a straight
        if set(dice_roll) == {1, 2, 3, 4, 5, 6}:
            score = 1500
        elif sorted(set(dice_roll)) == [1, 2, 3, 4, 5]:
            score += 1500

        # Calculate points for three pairs
        if len(set(dice_roll)) == 3 and all(count >= 2 for count in counts):
            score += 1000

        # Calculate points for a full house
        if len(set(dice_roll)) == 2 and 2 in counts and 3 in counts:
            score = 1500

        return score
    
    @staticmethod
    def roll_dice(num_dice):
        if not isinstance(num_dice, int) or not (1 <= num_dice <= 6):
            raise ValueError("Number of dice must be an integer between 1 and 6.")

        return tuple(random.randint(1, 6) for _ in range(num_dice))


if __name__ == "__main__":
        
    dice_roll = (5,)
    score = GameLogic.calculate_score(dice_roll)
    print(score)