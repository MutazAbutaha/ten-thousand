try:
    from ten_thousand.game_logic import GameLogic
except:
    from game_logic import GameLogic
def play():
    GameLogic().play_game()
class Game(GameLogic):
    def play(self):
         GameLogic().play_game()
if __name__ == "__main__":
    play()