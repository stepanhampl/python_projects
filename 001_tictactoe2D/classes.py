# class Box:
#     pass

class Field:  # grid

    def __init__(self, dimensions: tuple[int, int]):  # accepts dimensions
        """checks inputed tuple and creates placeholder - two-dimensional list, besides creating object"""
        self.width = dimensions[0]
        self.height = dimensions[1]

        if self.width > 30 and self.width < 3 or self.height > 99 and self.height < 3:
            raise Exception("Sorry, width must be between 3 and 30, height between 3 and 99")  # width: because it wouldnt fit in window...
        self.rows = []
        for _ in range(self.height):
            self.rows.append([' '] * self.width)    # set up 'empty' boxes while init
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
        header_sequence = list(range(1, self.width + 1))          # [1, 2, 3, 4, 5]
        header_sequence = [str(num) if len(str(num)) > 1 else ' ' + str(num) for num in header_sequence]   # ['1', '2', '3', '4', '5']
        rendered_field = 'Y' + u'\u2193' + 'X' + u'\u2192' + ') '.join(header_sequence) + ')\n'    # 'y, arrow, x, arrow  1) 2) 3) 4) 5)' ...example = row number 0
        for i, row in enumerate(rows):         # add each row
            index = i + 1  # so it doesnt start with 0
            first_col_num = ' ' + str(index) if index < 10 else str(index)      # e.g. ' 5)' or '50)' ... second time no space
            rendered_field += first_col_num + ') ' + ' T '.join(row) + '\n'  # add box in left column... '1) ' AND add row itself
        return rendered_field


    # def render(self):
    #     boxes = list(self.rows)
    #     rendered_field = ''
    #     for index, box in enumerate(boxes):
    #         if index % self.width == 0:
    #             rendered_field += box + '\n'
    #         else:    
    #             rendered_field += box + '|'
    #     return rendered_field  # returns string with newline chars - it will be printed

class Sign(Field):  # both X and O
    def __init__(self, location: tuple[int, int], which: str):
        self.x_axis = location[0]
        self.y_axis = location[1]
        self.which = which


class Ex(Sign):  # X
    def __init__(self, location: tuple[int, int]):
        super().__init__(location, 'X')


class Oh(Sign):  # O
    def __init__(self, location: tuple[int, int]):
        super().__init__(location, 'O')
