from classes import *


# append new Sign to list, sort, ren


def run_game():
    width = int(input("Insert desired width of gamefield: "))
    height = int(input("Insert desired height of gamefield: "))
    playfield = Field((width, height))  # dimensions # init of playfield
    print(playfield.render())  # newly rendered playfield is printed


run_game()