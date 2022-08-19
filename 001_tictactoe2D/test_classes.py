import classes

# used inside test_status()


def assist_status(dimensions: tuple, winner, players, goal, rows):
    playfield = classes.Field(dimensions, goal, players)
    playfield.rows = rows
    status = playfield.status()
    assert status == winner


def test_status():
    winner = 'X'
    players = ('X', 'O')
    goal = 3
    dimensions = (3, 3)
    # test horizontal evaluation
    rows = [['X', 'X', 'X'], ['O', 'O', ' '], ['O', ' ', ' ']]
    assist_status(dimensions, winner, players, goal, rows)
    rows = [['X', 'O', 'O'], ['O', 'O', ' '], ['X', 'X', 'X']]
    assist_status(dimensions, winner, players, goal, rows)
    rows = [['X', 'O', 'X'], ['O', 'O', 'O'], ['X', ' ', ' ']]
    winner = 'O'
    assist_status(dimensions, winner, players, goal, rows)
    # test another players
    rows = [['Ň', 'Ř', 'Ň'], ['Ř', 'Ř', 'Ř'], ['Ň', ' ', ' ']]
    players = ('Ř', 'Ň')
    assist_status(dimensions, 'Ř', players, goal, rows)
    # test bigger goal, bigger field
    rows = [
        [' ', ' ', ' ', ' ', ' ', ' '],
        ['O', 'X', 'O', 'O', 'X', 'O'],
        [' ', ' ', ' ', ' ', ' ', ' '],
        ['O', 'O', 'X', 'O', 'O', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        ['O', 'X', 'X', 'X', 'X', 'X'], ]
    dimensions = (6, 6)
    goal = 5
    winner = 'X'
    players = ('X', 'O')
    assist_status(dimensions, winner, players, goal, rows)
    # empty field
    winner = True       # True ~ go on
    players = ('X', 'O')
    goal = 3
    dimensions = (3, 3)
    rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assist_status(dimensions, winner, players, goal, rows)
    # almost empty field
    rows = [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assist_status(dimensions, winner, players, goal, rows)
    winner = 'X'
    players = ('X', 'O')
    goal = 3
    dimensions = (3, 3)
    # test horizontal evaluation
    rows = [['X', 'X', 'X'], ['O', 'X', 'O'], ['O', 'O', 'X']]
    assist_status(dimensions, winner, players, goal, rows)

    # test draw
    winner = False
    rows = [['O', 'X', 'O'], 
            ['X', 'X', 'O'], 
            ['O', 'O', 'X']]
    assist_status(dimensions, winner, players, goal, rows)
    # # wide, diagonal, right
    winner = 'X'
    players = ('X', 'O')
    goal = 3
    dimensions = (6, 3)
    rows = [[' ', ' ', ' ', 'X', ' ', ' '], [' ', ' ', ' ', ' ', 'X', ' '], [' ', ' ', ' ', ' ', ' ', 'X']]
    assist_status(dimensions, winner, players, goal, rows)    
    # wide, diagonal, left
    rows = [[' ', ' ', ' ', 'X', ' ', ' '], [' ', ' ', 'X', ' ', ' ', ' '], [' ', 'X', ' ', ' ', ' ', ' ']]
    assist_status(dimensions, winner, players, goal, rows)