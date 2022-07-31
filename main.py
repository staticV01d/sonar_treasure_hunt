import sonar as game

print('S O N A R !\n')

if input('Would you like to view the instructions? (yes/no) ').lower().startswith('y'):
    game.show_instructions()

while True:
    sonar_devices = 20
    board = game.get_new_board()
    chests = game.get_random_chests(3)
    game.draw_board(board)
    prev_moves = []

    while sonar_devices > 0:
        print(f'You have {sonar_devices} sonar device(s) and {len(chests)} treasure chests remaining.')

        x, y = game.enter_player_move(prev_moves)
        prev_moves.append([x, y])

        move_result = game.make_move(board, chests, x, y)
        if not move_result:
            continue
        else:
            if move_result == 'You have found a sunken treasure chest!':
                for x, y in prev_moves:
                    game.make_move(board, chests, x, y)
            game.draw_board(board)
            print(move_result)

        if len(chests) == 0:
            print('You have found all the sunken treasure chests! Congratulations!')
            break

        sonar_devices -= 1

    if sonar_devices == 0:
        print("We've run out of sonar devices! Now we have to turn the ship around and head for home with treasure"
              "chests still out there! Game Over.\n    The remaining chests were here:")
        for x, y in chests:
            print(f'    {x}, {y}')

    if not input('Would you like to play again? (yes/no) ').lower().startswith('y'):
        game.exit_game()
