

def evaluate(field, players):  # True if game ends
    """says, who won if someone did"""  # three same signs in a row are necessary
    for i in range(len(field)-2):     # iterate through field, but skip last two elements, since they're included in the if below
        if field[i] in players and field[i] == field[i + 1] and field[i] == field[i + 2]:
            print(f'{field[i].strip().upper()} won! Yaaaay!!!')
            return True  # when there is 'xxx' or 'ooo' in a row
    if ' - ' not in field:
        print("It's a draw!")
        return True
    return False


def input_ok(usr_input, field, players):    # true if can be placed
    """says, if x or o can be placed on certain place (usr_input)"""
    return usr_input in range(len(field)) and field[usr_input] not in players

def get_input(player, players, field):
    while True:  # repeats untill user inputs number of an empty box
        move = int(
            input(f"Now, it is {player.strip().upper()}'s move. Waiting for number..."))
        if input_ok(move, field, players):
            # add player to certain position
            field[move] = player
            break                            # end loop
        else:
            print(f'Nope, {move} is already full or out of range.')


def tictactoe1d(width):
    if width > 100:
        raise ValueError('width is too high')
    players = [" x ", " o "]
    header = [f"0{str(x)}_" if len(str(x)) == 1 else f"{str(x)}_" for x in list(range(width))]
    field = [" - "] * width  # [' - ', ' - ', ... ]
    # header = list(range(width))  # [0,1,2,3...]
    for _ in range(width):                   # repeat width times
        for player in players:            # repeat twice, player switches between "X" an "O"
            # prints all elements of header separated by nothing
            print(*header, sep="")

            get_input(player, players, field)

            # didnt someone won right now? (or Is field full and it's a tie?)
            if evaluate(field, players):
                exit()  # the problem ############################ return??
            # print every value of field[] separated by nothing
            print(*field, sep="")

tictactoe1d(10)