import classes


def run_game():
    width = int(input("Insert desired width of gamefield: "))
    height = int(input("Insert desired height of gamefield: "))
    how_many_to_win = 3     # how many do you need to have in a row to win
    players = ('X', 'O')        # probably can be more than 2
    playfield = classes.Field((width, height), how_many_to_win, players)  # dimensions # init of playfield
    main_game_loop(playfield, players)


def keep_going(playfield, players):
    status = playfield.status()
    if status == True:  # if game goes on
        print('debugSTATUS1: ' + str(status))
        return True     # go on
    elif status == False: 
        print('debugSTATUS2: ' + str(status))
        print("It's a draw")
        return False
    elif status in players:
        print('debugSTATUS3: ' + str(status))
        print(f"Congratualtions, {status} won")
        return False


def get_and_use_input(player, playfield):
    while True:
        print(f"{player}'s turn:")
        x_axis = int(input('Where on x-axis?'))
        y_axis = int(input('Where on y-axis?'))
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
                print(playfield.render())  # newly rendered playfield is printed
                return


run_game()