import sys
import random
import math

def get_new_board():
    """Create new 60x15 board data structure."""
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def draw_board(board: list[list]):
    """Draw a new board data structure."""
    tens_digits_line = '    '
    for i in range(1, 6):
        tens_digits_line += (' ' * 9) + str(i)

    print(tens_digits_line)
    print('   ' + ('0123456789' * 6) + '\n')

    for row in range(15):
        if row < 10:
            extra_space = ' '
        else:
            extra_space = ''

        board_row = ''
        for column in range(60):
            board_row += board[column][row]

        print(f"{extra_space}{row} {board_row} {row}")
    print('\n' + '   ' + ('0123456789' * 6))
    print(tens_digits_line)

def get_random_chests(num_chests: int):
    """Create treasure chest coordinate data."""
    chests = []
    while len(chests) < num_chests:
        new_chest = [random.randint(0, 59), random.randint(0, 14)]
        if new_chest not in chests:
            chests.append(new_chest)

    return chests

def is_on_board(x: int, y: int):
    """Determines if the given coordinates are on the board.

    Returns: True if point exists on board, otherwise False"""
    return 0 <= x <= 59 and 0 <= y <= 14

def make_move(board: list[list], chests: list[list[int]], x: int, y: int):
    """Change the board data structure with a sonar device character."""
    least_distance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
        if distance < least_distance:
            least_distance = distance

    least_distance = round(least_distance)

    if least_distance == 0:
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if least_distance < 10:
            board[x][y] = str(least_distance)
            return f'Treasure detected at a distance of {least_distance} from the sonar device.'
        else:
            board[x][y] = 'X'
            return 'Sonar did not detect anything. All remaining treasure chests are out of range.'

def enter_player_move(previous_moves):
    """Let the player enter their move.

    Returns:  Two-item list of int x/y coords"""
    print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == "quit":
            print('Thank you for playing!')
            exit_game()

        move = move.split()
        x, y = int(move[0]), int(move[1])
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and is_on_board(x, y):

            if [x, y] in previous_moves:
                print('You have already given these coordinates.')
                continue
            return [x, y]

        print('Enter a number from 0 to 59, a space, then a number from 0 to 14')

def show_instructions():
    print("""Instructions:
    You are the captain of the S.S. Minnow Johnson, a treasure-hunting ship.
    Your current mission:
    Use sonar devices to find three sunken treasure chests at the bottom of the ocean.
    You could only afford simple sonar that returns distance, not direction.
    Enter coordinates for where to drop sonar device. 
    The ocean map will be marked with the distance to the nearest chest.
    Or an 'X' if no chests are detected in the range of the device.
    Example: A 'C' marks where the chests are located. A mark of '3' means a chest is 3 spaces away.
    
               1         2         3
     012345678901234567890123456789012
    
    0 ~~``~~`~~~`~~~``~~~~~~``~~````~` 0
    1 `~~``~~``~~~~```~~~`~~~``~~``~~` 1
    2 `~`C``3~~```C~~~``~~`~~````~~`~` 2
    3 ~~`~~~``~~~~~~```~``~`~~`~~```~~ 3
    4 ``~~~```~~``C~`~``~~~~``~~~`~~`~ 4
    
      012345678901234567890123456789012 
                1         2         3
    (in actual game, chests are not visible)
    
    Press enter to continue...""")

    input()
    print("""When you drop a sonar device directly on a chest retrieve it and the other devices update to show how far 
    away the next chest is.
    The chests are beyond the range of the sonar device on the left, so it shows an 'X'.
    
               1         2         3
     012345678901234567890123456789012
     
    0 ~~~`~~~```~~```~~`~``~`~~~``~``~ 0
    1 ~~~``~~````~`~~~~~`~~````~~~``~~ 1
    2 ``~X``7`~~~~`C~~~~~``~~~~``~~``` 2
    3 ``~~```````~```~~~~~~```~~~~```~ 3
    4 `~``~~~~````~C~~~~```~`~`~~~~``~ 4
    
                1         2         3  
      012345678901234567890123456789012
      
    The treasure chests do not move around. Sonar devices can detect treasure chests up to a distance of 9 spaces.
    Try to collect all 3 chests before running out of sonar devices. Good Luck!
    
    Press enter to continue...""")
    input()

def exit_game():
    sys.exit()
