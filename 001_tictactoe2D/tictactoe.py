from operator import truediv
from classes import *


def run_game():
    width = int(input("Insert desired width of gamefield: "))
    height = int(input("Insert desired height of gamefield: "))
    playfield = Field((width, height))  # dimensions # init of playfield
    main_game_loop(playfield, ('X', 'O'))


def keep_going(playfield, players):
    if status := playfield.status() == True:  # if game goes on
        return True
    elif status == False:
        print("It's a draw")
        return False
    elif status in players:
        print(f"Congratualtions, {status} won")
        return False


def main_game_loop(playfield, players):
    while True:  # while game doesn't end
        for player in [players[0], players[1]]:
            print(playfield.render())  # newly rendered playfield is printed
            while True:
                print(f"{player}'s turn:")
                x_axis = int(input('Where on x-axis?'))
                y_axis = int(input('Where on y-axis?'))
                # False if box is full, otherwise True # saves player's move - it will be shown by the next playfield.render()
                if message := playfield.add_move((x_axis, y_axis), player):
                    print(f'Sorry, {message}.')
                else:
                    break
            if not keep_going(playfield, players):
                print(playfield.render())  # newly rendered playfield is printed
                return



run_game()
