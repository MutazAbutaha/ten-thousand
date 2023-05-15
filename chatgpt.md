## calculate method :
prompt 1 : create GameLogic class and Add calculate_score static method to GameLogic class and
The input to calculate_score is a tuple of integers that represent a dice roll and
The output from calculate_score is an integer representing the roll’s score according to rules of game.

actual code : 
```python code 
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

            # Calculate additional points for individual ones and fives
            if face_value == 1:
                score += count * 100
            elif face_value == 5:
                score += count * 50

        return score

```

prompt 2 : These are the base methods of scoring:

Single fives are worth 50 points
Single ones are worth 100 points
Three of a kind are worth 100 points times the number rolled, except for three ones which are worth 1000 points
If four, five, or six of a kind are rolled, each additional dice doubles the amount of dice previously rolled. For example, 4 die showing the number 3 would be 600 points and 5 die showing the number 3 would be 1200 points
This makes the highest possible score in a single roll 8000 for six ones (1000 for three ones, after that player multiplies the roll by two for each additional one in that series of rolling.)
A straight from 1 to 6 is worth 1500 points. If a player fails to roll a straight, they may make one attempt to complete the straight. If the desired number(s) does not turn up on the next roll, that round is a "crap out" even if there are scoring dice on the table i.e. 1's or 5's.
Three pairs are worth 1000 points, for instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise (some places have their own house rules).
Full house (3 of a kind plus 2 of a kind) are worth 1,500

actual code : 
```python code 
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
            if count >= 4:
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
```

## Dice roll method :
prompt 3 : Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.

actual code : 
```python code 
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        # ... existing code ...

    @staticmethod
    def roll_dice(num_dice):
        if not isinstance(num_dice, int) or not (1 <= num_dice <= 6):
            raise ValueError("Number of dice must be an integer between 1 and 6.")

        return tuple(random.randint(1, 6) for _ in range(num_dice))
```
