# class Box:
#     pass

class Field:  # grid

    def __init__(self, dimensions: tuple[int, int]):  # accepts dimensions
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.boxes = [" "] * (self.width * self.height)  # creates list of boxes

    def render(self):
        boxes = list(self.boxes)
        rendered_field = ''
        for index, box in enumerate(boxes):
            if index % self.width == 0:
                rendered_field += box + '\n'
            else:    
                rendered_field += box + '|'
        return rendered_field  # returns string with newline chars - it will be printed

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
        super().__init__(location, 'Y')
