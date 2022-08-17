class Field:  # grid

    def __init__(self, dimensions: tuple[int, int]):  # accepts dimensions
        """checks inputed tuple and creates placeholder - two-dimensional list, besides creating object"""
        self.width = dimensions[0]
        self.height = dimensions[1]

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

    def add_move(self, location: tuple[int, int], which: str):      # False if loop should stop
        """inserts move into 'rows' list, but if move is invalid returns string with reason 
        (it means if box is full or out of range), otherwise False"""
        x = location[0]     # x-axis
        y = location[1]     # y-axis
        validate = self.validate_move(x, y)     # False if box is empty and exists
        if not validate:    # box is empty and exists
            self.rows[y - 1][x - 1 : x] = which
        return validate


# class Sign(Field):  # both X and O
#     def __init__(self, location: tuple[int, int], which: str):
#         x_axis = location[0]
#         y_axis = location[1]
#         super().insert_in_rows(x_axis, y_axis)
