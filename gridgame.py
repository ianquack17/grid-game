
# grid for the game w/ starting positions
grid = {0:[1,2,3,'y'],
        1:[5,6,7,8],
        2:[9,10,11,12],
        3:['x',14,15,16]}

# temporary veriables for spots underneath x and y
user_temp = 13
cpu_temp = 4

user_score = 0
cpu_score = 0

# used to find the current positions of either the player or computer
def find_position(d, value):
    for key, lst in d.items():
        if value in lst:
            return key, lst.index(value)
    return None, None


def _dmove(direction, player, temp):
    '''
    Function for movement in each direction.

    Parameters:
        -direction(str): what direction to go in.
        -player(str): which player to move
        -temp(str): which temporary variable to use

    Returns:
        +New grid with moved icons
    '''

    # Command for if y wins the game
    if direction == 'x':
        print(f'CPU wins the game!')
        cpu_win = True
        return cpu_win

    # Find position of current player
    player_position = find_position(grid,player)
    player_key = player_position[0]
    player_value = player_position[1]

    direction_index = find_position(grid, direction)
    direction_key = direction_index[0]
    direction_value = direction_index[1]

    # Change current position value to temp value
    grid[player_key][player_value] = temp

    # Change temp to the value the player is taking
    temp = direction

    # Change the value to below the current value to player icon
    grid[direction_key][direction_value] = player

    # Update the user position
    player_position = find_position(grid, player)
    player_key = player_position[0]
    player_value = player_position[1]


def _player_turn(player,temp):
    while True:
        """
        Function for each player turn

        Parameters:
            player(str): string of player name.
            temp(str): string for temp to change based on player.

        Returns:
            Modified game grid based on players chosen movement
        """

        # Find position of current player
        player_position = find_position(grid,player)
        player_key = player_position[0]
        player_value = player_position[1]

        # Move commands
        right = grid[player_key][player_value + 1] if player_value + 1 < len(grid[player_key]) else None
        left = grid[player_key][player_value - 1] if player_value - 1 >= 0 else None
        up = grid[player_key - 1][player_value] if player_key - 1 >= 0 else None
        down = grid[player_key + 1][player_value] if player_key + 1 < len(grid) else None

        # Movement input
        move = input(f'Player {player}, Where are you moving? ')
        if move == 'r':
            if player_value == 3:
                print("Cannot move there")
            else:
                _dmove(right, player, temp)
                break
        elif move == 'l':
            if player_value == 0:
                print("Cannot move there")
            else:
                _dmove(left, player, temp)
                break
        elif move == 'u':
            if player_key == 0:
                print("Cannot move there")
            else:
                _dmove(up, player, temp)
                break
        elif move == 'd':
            if player_key == 3:
                print("Cannot move there")
            else:
                _dmove(down, player, temp)
                break
    return player_position

def _cpu_turn(player,temp,player_position):
    player_key = player_position[0]
    player_value = player_position[1]

    cpu_position = find_position(grid,'y')
    cpu_key = cpu_position[0]
    cpu_value = cpu_position[1]

    key_difference = player_key - cpu_key
    value_difference = player_value - cpu_value

    right = grid[cpu_key][cpu_value + 1] if cpu_value + 1 < len(grid[cpu_key]) else None
    left = grid[cpu_key][cpu_value - 1] if cpu_value - 1 >= 0 else None
    up = grid[cpu_key - 1][cpu_value] if cpu_key - 1 >= 0 else None
    down = grid[cpu_key + 1][cpu_value] if cpu_key + 1 < len(grid) else None

    if key_difference == value_difference or key_difference < value_difference:
        if key_difference < 0:
            _dmove(up, player, temp)
        elif key_difference > 0:
            _dmove(down, player, temp)
    elif key_difference > value_difference:
        if value_difference < 0:
            _dmove(left, player, temp)
        elif value_difference > 0:
            _dmove(right, player, temp)




    
score = 0

# Start game loop
while True:
    # Print grid
    grid_print = (f'{grid[0]} \n{grid[1]} \n{grid[2]} \n{grid[3]}')
    print(grid_print)

    _player_turn('x',user_temp)
    score += 1
    print(f'User score: {score}')

    player_position = _player_turn('x', user_temp)

    if score == 10:
        print(f'Player X Wins!')
        break

    # Print grid
    grid_print = (f'{grid[0]} \n{grid[1]} \n{grid[2]} \n{grid[3]}')
    print(grid_print)

    _cpu_turn('y',cpu_temp,player_position)
