
# grid for the game w/ starting positions
grid = {0:[1,2,3,'y'],
        1:['x',6,7,8],
        2:[9,10,11,12],
        3:[13,14,15,16]}

# temporary veriables for spots underneath x and y
temp = 5
cpu_temp = 4

# used to find the current positions of either the player or computer
def find_position(d, value):
    for key, lst in d.items():
        if value in lst:
            return key, lst.index(value)
    return None, None


# print statement of the key and index of position
user_position = find_position(grid, 'x')
user_key = user_position[0]
user_value = user_position[1]

# Start game loop
while True:
    # Print grid
    grid_print = (f'{grid[0]} \n{grid[1]} \n{grid[2]} \n{grid[3]}')
    print(grid_print)
    # gets the current value of the positions relative to the player
    right = grid[user_key][user_value + 1]
    left = grid[user_key][user_value - 1]
    up = grid[user_key - 1][user_value]
    down = grid[user_key + 1][user_value]
    move = input("Where are you moving? ")
    if move == 'r':
        # Find the index of the value to the right
        right_index = find_position(grid, right)
        right_key = right_index[0]
        right_value = right_index[1]

        # Change current position value to temp value
        grid[user_key][user_value] = temp

        # Change temp to the value the player is taking
        temp = right

        # Change the value to the right of current value to player icon
        grid[user_key][right_value] = 'x'
        
        # Update the user position
        user_position = find_position(grid, 'x')
        user_key = user_position[0]
        user_value = user_position[1]
    elif move == 'l':
        # Find the index of the value to the left
        left_index = find_position(grid,left)
        left_key = left_index[0]
        left_value = left_index[1]

        # Change current position value to temp value
        grid[user_key][user_value] = temp

        # Change temp to the value the player is taking
        temp = left

        # Change the value to the left of current value to player icon
        grid[left_key][left_value] = 'x'

        # Update the user position
        user_position = find_position(grid, 'x')
        user_key = user_position[0]
        user_value = user_position[1]
    elif move == 'u':
        # Find the index of the value above
        up_index = find_position(grid, up)
        up_key = up_index[0]
        up_value = up_index[1]

        # Change current position value to temp value
        grid[user_key][user_value] = temp

        # Change temp to the value the player is taking
        temp = up

        # Change the value above the current value to player icon
        grid[up_key][up_value] = 'x'
        
        # Update the user position
        user_position = find_position(grid, 'x')
        user_key = user_position[0]
        user_value = user_position[1]
    elif move == 'd':
        # Find the index of the value below
        down_index = find_position(grid, down)
        down_key = down_index[0]
        down_value = down_index[1]

        # Change current position value to temp value
        grid[user_key][user_value] = temp

        # Change temp to the value the player is taking
        temp = down

        # Change the value to below the current value to player icon
        grid[down_key][down_value] = 'x'
        
        # Update the user position
        user_position = find_position(grid, 'x')
        user_key = user_position[0]
        user_value = user_position[1]



