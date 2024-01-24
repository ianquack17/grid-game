
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

        # Movement input
        move = input(f'{player} Where are you moving? ')
        if move == 'r':
            # Find the index of the value to the right
            right_index = find_position(grid, right)
            right_key = right_index[0]
            right_value = right_index[1]

            # Change current position value to temp value
            grid[player_key][player_value] = temp

            # Change temp to the value the player is taking
            temp = right

            # Change the value to the right of current value to player icon
            grid[right_key][right_value] = player

            # Update the user position
            player_position = find_position(grid, player)
            player_key = player_position[0]
            player_value = player_position[1]
        elif move == 'l':
            # Find the index of the value to the left
            left_index = find_position(grid,left)
            left_key = left_index[0]
            left_value = left_index[1]

            # Change current position value to temp value
            grid[player_key][player_value] = temp

            # Change temp to the value the player is taking
            temp = left

            # Change the value to the left of current value to player icon
            grid[left_key][left_value] = player

            # Update the user position
            player_position = find_position(grid, player)
            player_key = player_position[0]
            player_value = player_position[1]
        elif move == 'u':
            # Find the index of the value above
            up_index = find_position(grid, up)
            up_key = up_index[0]
            up_value = up_index[1]

            # Change current position value to temp value
            grid[player_key][player_value] = temp

            # Change temp to the value the player is taking
            temp = up

            # Change the value above the current value to player icon
            grid[up_key][up_value] = player

            # Update the user position
            player_position = find_position(grid, player)
            player_key = player_position[0]
            player_value = player_position[1]
        elif move == 'd':
            # Find the index of the value below
            down_index = find_position(grid, down)
            down_key = down_index[0]
            down_value = down_index[1]

            # Change current position value to temp value
            grid[player_key][player_value] = temp

            # Change temp to the value the player is taking
            temp = down

            # Change the value to below the current value to player icon
            grid[down_key][down_value] = player

            # Update the user position
            player_position = find_position(grid, player)
            player_key = player_position[0]
            player_value = player_position[1]

    score = 0

    _player_turn('x',user_temp)

    # Print grid
    grid_print = (f'{grid[0]} \n{grid[1]} \n{grid[2]} \n{grid[3]}')
    print(grid_print)

    _player_turn('y',cpu_temp)



    
