from collections import deque, defaultdict
import random
from array import array


class Dice:

    def __init__(self):
        self._sides = 6

    @property
    def sides(self):
        return self._sides
    
    @sides.setter
    def sides(self, value):
        if not 0 < value < 101:
            raise ValueError('Count of dice sides must be from 1 to 100')
        self._sides = value


class Game:

    def __init__(self):
        self._dice_amount = 0
        self.throws_history = deque(maxlen=100)

    @property
    def dice_amount(self):
        return self._dice_amount
    
    @dice_amount.setter
    def dice_amount(self, value):
        if not 0 < value < 6:
            raise ValueError('Game supports from 1 to 5 dices')
        self._dice_amount = value
    
    def play(self, throws, sides):
        throws_results = []
        for _ in range(throws):
            throw_result = [random.randint(1, sides) for _ in range(self._dice_amount)]
            throws_results.append(throw_result)
            self.throws_history.append((sides, throw_result))
        return throws_results
    
            
def collect_users_input():
    dice_amount = int(input('How many dices you want to throw?'))
    sides = int(input('Pick number of sides for dice:'))
    throws = int(input('Choose how many times you want to throw dice and'\
                           'start the game!'))
    return dice_amount, sides, throws

def collect_next_action():
    next_action = ''
    while next_action not in ["p", "e", "s"]:
        next_action = input('Type "p" - play again, "e" - end game'\
                            ' , "s" - see throws history')
    return next_action


if __name__ == '__main__':
    
    dice = Dice()
    game = Game()
    game_on = True
    while game_on:
        game.dice_amount, dice.sides, throws = collect_users_input()
        for item in game.play(throws, dice.sides):
            print(item)
        next_action = collect_next_action()
        while next_action == 's':
            [print(item) for item in list(game.throws_history)]
            next_action = collect_next_action()
        if next_action == 'e':
            game_on = False
            
        
