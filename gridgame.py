
# grid for the game w/ starting positions
grid = {0:[1,2,3,4],
        1:['x',6,7,8],
        2:['y',10,11,12],
        3:[13,14,15,16]}

# temporary veriables for spots underneath x and y
user_temp = 5
cpu_temp = 9

# used to find the current positions of either the player or computer
def find_position(d, value):
    for key, lst in d.items():
        if value in lst:
            return key, lst.index(value)
    return None, None


# Start game loop
while True:
    # Print grid
    grid_print = (f'{grid[0]} \n{grid[1]} \n{grid[2]} \n{grid[3]}')
    print(grid_print)

    def _player_turn(player,temp):
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
        print(player_position)

        # Move commands
        right = grid[player_key][player_value + 1] if player_value + 1 < len(grid[player_key]) else None
        left = grid[player_key][player_value - 1] if player_value -1 >= 0 else None
        up = grid[player_key - 1][player_value] if player_key - 1 >= 0 else None
        down = grid[player_key + 1][player_value] if player_key + 1 < len(grid) else None

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

        # Movement input
        move = input(f'Player {player}, Where are you moving? ')
        if move == 'r':
            _dmove(right, player, temp)
        elif move == 'l':
            _dmove(left, player, temp)
        elif move == 'u':
            _dmove(up, player, temp)
        elif move == 'd':
            _dmove(down, player, temp)

    score = 0

    _player_turn('x',user_temp)

    # Print grid
    grid_print = (f'{grid[0]} \n{grid[1]} \n{grid[2]} \n{grid[3]}')
    print(grid_print)

    _player_turn('y',cpu_temp)



    
