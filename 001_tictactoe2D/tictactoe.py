from classes import *


# append new Sign to list, sort, ren


def run_game():
    width = int(input("Insert desired width of gamefield: "))
    height = int(input("Insert desired height of gamefield: "))
    playfield = Field((width, height))  # dimensions # init of playfield

    while True:  # while game doesn't end
        for player in ['X', 'O']:
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
            if status := playfield.status() != True:  # if game ends # if status explicitly doesn't equal True
                if status == False:
                    print("It's a draw")
                else:
                    print(f"Congratualtions, {status} won")
                break


run_game()
