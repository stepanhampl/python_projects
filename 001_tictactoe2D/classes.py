class Evaluate():     # find winner

    def __init__(self, rows, players, goal):
        """just for inputing data (what values search for, list to search in, how many need to be in a row)"""
        self.rows = rows            # list to search in
        self.players = players      # what values to search for
        self.goal = goal

    def horizontal(self):
        """checks for horizontal row with specified length made by one player"""
        for row in self.rows:
            for index, box in enumerate(row[:len(row)-(self.goal-1)]):     # if goal is 3, two last will not be used in this for loop

                if row[index+1:index+(self.goal)] == [box] *(self.goal-1):        # if goal is 3, compares box with next 2 items
                    return box      # equals to one of the players

        return False

    def vertical(self):
        """checks for vertical row with specified length made by one player"""
        return False

    def diagonal(self):
        """checks for diagonal row with specified length made by one player"""
        return False

    def total(self):
        """brings all poossible ways to win into one method.
        False if nobody won"""
        if ((win := self.horizontal()) or (win := self.vertical()) or (win := self.diagonal())):
            print('debugWIN: ' + win)
            return win      # returns character, that won
        else:
            return False
            # return False


class Field():      # grid

    # accepts dimensions
    def __init__(self, dimensions: tuple[int, int], how_many_to_win, players):
        """checks inputed tuple and creates placeholder - two-dimensional list, besides creating object"""
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.goal = how_many_to_win
        self.players = players

        if self.width > 30 and self.width < 3 or self.height > 99 and self.height < 3:
            # width: because it wouldnt fit in window...
            raise Exception(
                "Sorry, width must be between 3 and 30, height between 3 and 99")
        self.rows = []
        for _ in range(self.height):
            # set up 'empty' boxes while init
            self.rows.append([' '] * self.width)
        # now    # self.rows = [ [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '] ]
        # later  # self.rows = [ ['X', ' ', ' ', ' '], ['O', 'X', ' ', ' '], [' ', 'X', ' ', 'O'], ['X', ' ', ' ', ' '], [' ', 'O', 'O', ' '] ]

    def status(self):
        """Returns status of the game. 
        True if game goes on; 
        'X' or 'O' if there is a winner; 
        False if it is a draw (full field, but no one wins)."""

        # winner
        eval = Evaluate(self.rows, self.players, self.goal)
        winner = eval.total()
        print('debugWINNER: ' + str(winner))
        if winner:     # if there is a winner
            return winner
        # list of Trues, or empty list if gamefield is full
        if True not in [True for row in self.rows if ' ' in row]:
            return False
        return True   # just for now

    def render(self):
        """creates multiline string, which is current gamefield when printed"""
        rows = list(self.rows)
        header_sequence = list(range(1, self.width + 1)
                               )          # [1, 2, 3, 4, 5]
        header_sequence = [str(num) if len(str(num)) > 1 else ' ' + str(num)
                           for num in header_sequence]   # ['1', '2', '3', '4', '5']
        # 'y, arrow, x, arrow  1) 2) 3) 4) 5)' ...example = row number 0
        rendered_field = 'Y' + u'\u2193' + 'X' + \
            u'\u2192' + ') '.join(header_sequence) + ')\n'
        for i, row in enumerate(rows):         # add each row
            index = i + 1  # so it doesnt start with 0
            # e.g. ' 5)' or '50)' ... second time no space
            first_col_num = ' ' + str(index) if index < 10 else str(index)
            # add box in left column... '1) ' AND add row itself
            rendered_field += first_col_num + ') ' + ' T '.join(row) + '\n'
        return rendered_field

    def validate_move(self, x, y):
        """returns True if move can be inserted, otherwise returns False"""

        # is in correct range?
        if y < 1 or len(self.rows) < y:
            return 'y is out of range'
        if x < 1 or len(self.rows[y - 1]) < x:
            return 'x is out of range'

        if not self.rows[y - 1][x - 1] == ' ':
            return 'desired box is full'
        else:
            return False

    # False if loop should stop
    def add_move(self, location: tuple[int, int], which: str):
        """inserts move into 'rows' list, but if move is invalid returns string with reason 
        (it means if box is full or out of range), otherwise False"""
        x = location[0]     # x-axis
        y = location[1]     # y-axis
        # False if box is empty and exists
        validate = self.validate_move(x, y)
        if not validate:    # box is empty and exists
            self.rows[y - 1][x - 1: x] = which
        return validate


# class Sign(Field):  # both X and O
#     def __init__(self, location: tuple[int, int], which: str):
#         x_axis = location[0]
#         y_axis = location[1]
#         super().insert_in_rows(x_axis, y_axis)
