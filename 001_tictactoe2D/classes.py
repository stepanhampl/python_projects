class Evaluate():     # find winner

    def __init__(self, rows, players, goal):
        """just for inputing data (what values search for, list to search in, how many need to be in a row)"""
        self.rows = rows            # list to search in
        self.players = players      # what values to search for
        self.goal = goal

    def horizontal(self):
        """checks for horizontal row with specified length made by one player"""
        for row in self.rows:
            # if goal is 3, two last will not be used in this for loop
            for ibox, box in enumerate(row[:len(row)-(self.goal-1)]):
                if box not in self.players:     # if box is " "
                    continue        # go for next box
                # if goal is 3, compares box with next 2 items
                if row[ibox+1:ibox+(self.goal)] == [box] * (self.goal-1):
                    return box      # equals to one of the players

        return False

    def vertical(self):
        """checks for vertical row with specified length made by one player"""
        # skip last rows (self.goal - 1), because below them are not enough items to form column {self.goal}-items long
        for irow, row in enumerate(self.rows[:len(self.rows)-(self.goal-1)]):      
            for ibox, box in enumerate(row):
                if box not in self.players:     # if box is " "
                    continue        # go for next box
                has_won = True
                # starting at 1, because first box doesnt count - boxes after it are compared directly with it
                for i in range(1, self.goal):
                    if box != self.rows[irow + i][ibox]:     # if the first box is NOT the same as some of the boxes below
                        has_won = False     # is overriden, when something below is not the same
                if has_won:
                    return box

        return False

    def diagonal(self):
        """checks for diagonal row with specified length made by one player. 
        Right direction is default."""
        # first use normal field, next time flipped one (to test first right way, then left way)
        for rows2 in (self.rows, self.rows[::-1]):
            # dont care about {rows2 - 1} last rows, because it wouldn't make sense
            dont_use_edge = len(rows2) - (self.goal - 1)        # don't use vertically
            # loop_through = rows2[dont_use_edge:]
            loop_through = rows2[:dont_use_edge]

            for irow, row in enumerate(loop_through):
                # if goal is 3, two last will not be used in this for loop # same for horizontal
                dont_use_edge = len(row) - (self.goal - 1)      # don't use horizontally
                # loop_through = row[dont_use_edge:]
                loop_through = row[:dont_use_edge]

                for ibox, box in enumerate(loop_through):
                    if box not in self.players:     # if box is " "
                        continue        # go for next box
                    # if goal is 3, compares box with next 2 items # diagonally, right
                    has_won = True
                    
                    # starting at 1, because first box doesnt count - boxes after it are compared directly with 'box'
                    for i in range(1, self.goal):
                        # we need to go below and right, so increment row-index and increment box-index
                        box2 = rows2[irow + i][ibox + i]
                        if box != box2:
                            has_won = False
                    if has_won:
                        return box

        return False


    def total(self):
        """brings all poossible ways to win into one method.
        False if nobody won"""
        if ((win := self.horizontal()) or (win := self.vertical()) or (win := self.diagonal())):
            return win      # returns character, that won
        else:
            return False
            # return False


class Field():      # grid

    # accepts dimensions
    def __init__(self, valid_input: tuple[int, int], players):
        """checks inputed tuple and creates placeholder - two-dimensional list, besides creating object"""
        self.width = valid_input[0]
        self.height = valid_input[1]
        self.goal = valid_input[2]
        self.players = players

        self.rows = []
        for _ in range(self.height):
            # set up 'empty' boxes while init
            self.rows.append([' '] * self.width)
        # now    # self.rows = [ [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '] ]
        # later  # self.rows = [ ['X', ' ', ' ', ' '], ['O', 'X', ' ', ' '], [' ', 'X', ' ', 'O'], ['X', ' ', ' ', ' '], [' ', 'O', 'O', ' '] ]

    def validate_input(to_validate):
        """Checks if input is valid. If not, asks again and again, until it is. Returns valid input"""
        width = to_validate[0]
        height = to_validate[1]
        how_win = to_validate[2]

        w_range = range(3, 30)
        h_range = range(3, 100)

        while not width in w_range or not height in h_range:
            print('Sorry, your input was incorrect.')
            if not width in w_range:
                width = int(input("Width must be between 3 and 30. Insert width of gamefield: "))
            if not height in h_range:
                height = int(input("Height must be between 3 and 100. Insert height of gamefield: "))

        while not how_win <= width and not how_win <= height and how_win > 1:
            how_win = int(input("'How many in a row to win' must fit into field and bigger than 1. Insert again: "))
        return (width, height, how_win)

    def status(self):
        """Returns status of the game. 
        True if game goes on; 
        'X' or 'O' if there is a winner; 
        False if it is a draw (full field, but no one wins)."""

        # winner
        eval = Evaluate(self.rows, self.players, self.goal)
        winner = eval.total()
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