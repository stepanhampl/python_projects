import classes


def run_game():
    width = classes.Tools.input_check('integer',
        "Insert desired width of gamefield: ")
    height = classes.Tools.input_check('integer',
        "Insert desired height of gamefield: ")
    # how many do you need to have in a row to win
    how_win = classes.Tools.input_check('integer',"How many in a row to win: ")
    players = ('X', 'O')        # probably can be more than 2

    valid_input = classes.Tools.validate_input((width, height, how_win))
    # dimensions # init of playfield
    playfield = classes.Field(valid_input, players)
    main_game_loop(playfield, players)


def keep_going(playfield, players):
    status = playfield.status()
    if status == True:  # if game goes on
        return True     # go on
    elif status == False:
        print("It's a draw")
        return False
    elif status in players:
        print(f"Congratualtions, {status} won!!!!!!!!!")
        return False


def get_and_use_input(player, playfield):
    while True:
        print(f"{player}'s turn:")
        x_axis = classes.Tools.input_check('integer', 'Where on x-axis?')
        y_axis = classes.Tools.input_check('string', 'Where on y-axis?')
        # False if box is full, otherwise True # saves player's move - it will be shown by the next playfield.render()
        if message := playfield.add_move((x_axis, y_axis), player):
            print(f'Sorry, {message}.')
        else:
            break


def main_game_loop(playfield, players):
    while True:  # while game doesn't end
        for player in [players[0], players[1]]:
            print(playfield.render())  # newly rendered playfield is printed
            get_and_use_input(player, playfield)
            if not keep_going(playfield, players):
                # newly rendered playfield is printed
                print(playfield.render())
                return


run_game()
