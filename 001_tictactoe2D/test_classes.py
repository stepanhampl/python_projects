# import pytest
import classes

def test_status():
    width = 3
    height = 3
    how_many_to_win = 3     # how many do you need to have in a row to win
    players = ('X', 'O') 
    playfield = classes.Field((width, height), how_many_to_win, players)

    playfield.rows = [['X', 'X', 'X'], ['O', 'O', ' '], ['O', ' ', ' ']]
    status = playfield.status()
    assert status == 'X'