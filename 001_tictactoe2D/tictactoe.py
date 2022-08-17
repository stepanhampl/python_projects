from classes import *


# append new Sign to list, sort, ren


def run_game():
    width = int(input("Insert desired width of gamefield: "))
    height = int(input("Insert desired height of gamefield: "))
    playfield = Field((width, height))  # dimensions # init of playfield
    
    # while (status := playfield.status()):  # while game doesn't end
    print(playfield.render())  # newly rendered playfield is printed
        # for char in ['X', 'Y']:
        #     print(f"{char}'s turn:")
        #     x_axis = input('Where on x-axis?')
        #     y_axis = input('Where on y-axis?')

run_game()