import random

class Neighbors:
        def __init__(self, left=None, right=None, up=None, down=None):
            self.left = left
            self.right = right
            self.up = up
            self.down = down
            self.DIRECTIONS = [
                'up_to_down',
                'up_to_left',
                'up_to_right',
                'down_to_up',
                'down_to_left',
                'down_to_right',
                'left_to_right',
                'left_to_up',
                'left_to_down',
                'right_to_left',
                'right_to_down',
                'right_to_up',
                'crossing_to_left',
                'crossing_to_right',
                'crossing_to_down', 
                'crossing_to_up']
            
        def check_compatibility(self):
            # TODO: This Function seems to be wrong

            compatible_tiles = self.DIRECTIONS
            if self.right is None and self.left is None and self.up is None and self.down is None:
                return compatible_tiles
            
            if self.up == -1:
                to_remove = [
                    'up_to_down',
                    'down_to_up',
                    'up_to_left',
                    'left_to_up',
                    'up_to_right',
                    'right_to_up',
                    'left_to_right',
                    'right_to_left',
                    'crossing_to_left',
                    'crossing_to_right',
                    'crossing_to_down', 
                    'crossing_to_up'
                ]
                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            elif self.up in ['up_to_down','down_to_up', 'up_to_left', 'left_to_up', 'right_to_up', 'up_to_right', 'crossing_to_left', 'crossing_to_right', 'crossing_to_down', 'crossing_to_up']:
                to_remove = [
                    'left_to_right',
                    'right_to_left',
                    'down_to_left',
                    'down_to_right',
                    'left_to_down',
                    'right_to_down'
                ]
            
                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            elif self.up in ['down_to_left', 'down_to_right', 'left_to_down', 'right_to_down','right_to_left', 'left_to_right']:
                to_remove = [
                    'up_to_down',
                    'down_to_up',
                    'up_to_left', 
                    'left_to_up', 
                    'right_to_up', 
                    'up_to_right', 
                    'crossing_to_left', 
                    'crossing_to_right', 
                    'crossing_to_down', 
                    'crossing_to_up'
                ]
                
                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)
            
            if self.right == -1:
                to_remove = [
                    'left_to_right',
                    'right_to_left',
                    'up_to_right',
                    'right_to_up',
                    'down_to_right',
                    'right_to_down',
                    'crossing_to_left',
                    'crossing_to_right',
                    'crossing_to_down',
                    'crossing_to_up'
                ]

                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            elif self.right in ['up_to_down', 'down_to_up', 'up_to_left', 'left_to_up', 'down_to_left', 'left_to_down']:
                to_remove = [
                    'left_to_right',
                    'right_to_left',
                    'down_to_right',
                    'right_to_down',
                    'up_to_right',
                    'right_to_up',
                    'crossing_to_left',
                    'crossing_to_right',
                    'crossing_to_down',
                    'crossing_to_up'
                ]
                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)
            
            elif self.right in ['left_to_right', 'right_to_left', 'down_to_right', 'right_to_down', 'up_to_right', 'right_to_up', 'crossing_to_left', 'crossing_to_right', 'crossing_to_down', 'crossing_to_up']:
                to_remove = [
                    'up_to_down', 
                    'down_to_up', 
                    'up_to_left',
                    'left_to_up', 
                    'down_to_left', 
                    'left_to_down'
                ]

                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)
            
            if self.left == -1:
                to_remove = [
                    'left_to_down',
                    'down_to_left',
                    'left_to_up',
                    'up_to_left',
                    'left_to_right',
                    'right_to_left',
                    'crossing_to_left',
                    'crossing_to_right',
                    'crossing_to_down',
                    'crossing_to_up'
                ]

                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            elif self.left in ['up_to_down', 'down_to_up', 'down_to_right', 'right_to_down', 'up_to_right', 'right_to_up']:
                to_remove = [
                    'left_to_right',
                    'right_to_left',
                    'down_to_left',
                    'left_to_down',
                    'up_to_left',
                    'left_to_up',
                    'crossing_to_left',
                    'crossing_to_right',
                    'crossing_to_down',
                    'crossing_to_up'
                ]

                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            elif self.left in ['left_to_right','right_to_left', 'down_to_left', 'left_to_down', 'up_to_left', 'left_to_up', 'crossing_to_left', 'crossing_to_right', 'crossing_to_down', 'crossing_to_up']:
                to_remove = [
                    'up_to_down',
                    'down_to_up', 
                    'down_to_right', 
                    'right_to_down', 
                    'up_to_right', 
                    'right_to_up'
                ]

                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)             

            if self.down == -1:
                to_remove = [
                    'up_to_down',
                    'down_to_up',
                    'down_to_left',
                    'left_to_down',
                    'right_to_down',
                    'down_to_right',
                    'crossing_to_left', 
                    'crossing_to_right', 
                    'crossing_to_down', 
                    'crossing_to_up'
                ]

                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            elif self.down in ['up_to_down', 'down_to_up', 'left_to_down', 'down_to_left', 'right_to_down', 'down_to_right', 'crossing_to_left', 'crossing_to_right', 'crossing_to_down', 'crossing_to_up']:
                to_remove = [
                    'left_to_right',
                    'right_to_left',
                    'left_to_up',
                    'up_to_left',
                    'right_to_up',
                    'up_to_right',
                ]

                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            elif self.down in ['left_to_up', 'up_to_left', 'up_to_right', 'right_to_up', 'left_to_right', 'right_to_left']:
                to_remove = [
                    'up_to_down', 
                    'down_to_up', 
                    'left_to_down', 
                    'down_to_left', 
                    'right_to_down', 
                    'down_to_right', 
                    'crossing_to_left', 
                    'crossing_to_right', 
                    'crossing_to_down', 
                    'crossing_to_up']

                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            return compatible_tiles

class Map:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.grid_aux = [[None for _ in range(size)] for _ in range(size)]
        self.start_pos = (0, 0)
        self.generate()
        self.DIRECTIONS = [
                'up_to_down',
                'up_to_left',
                'up_to_right',
                'down_to_up',
                'down_to_left',
                'down_to_right',
                'left_to_right',
                'left_to_up',
                'left_to_down',
                'right_to_left',
                'right_to_down',
                'right_to_up',
                'crossing_to_left',
                'crossing_to_right',
                'crossing_to_down', 
                'crossing_to_up']

    def get_neighbor_position(self, position, direction):
        row, col = position
        if direction == 'up_to_down':
            return row - 1, col
        elif direction == 'up_to_left':
            return row, col - 1
        elif direction == 'up_to_right':
            return row, col + 1
        elif direction == 'down_to_up':
            return row + 1, col
        elif direction == 'down_to_left':
            return row, col - 1
        elif direction == 'down_to_right':
            return row, col + 1
        elif direction == 'left_to_right':
            return row, col + 1
        elif direction == 'left_to_down':
            return row - 1, col
        elif direction == 'left_to_up':
            return row + 1, col
        elif direction == 'right_to_left':
            return row, col - 1
        elif direction == 'right_to_down':
            return row - 1, col
        elif direction == 'right_to_up':
            return row + 1, col
        elif direction == 'crossing_to_left':
            return row, col - 1
        elif direction == 'crossing_to_right':
            return row, col + 1
        elif direction == 'crossing_to_down':
            return row - 1, col
        elif direction == 'crossing_to_up':
            return row + 1, col
        else:
            print(direction)

    def is_straight_tile(tile_type):
        return tile_type in ['up_to_down', 'down_to_up', 'left_to_right', 'right_to_left']

    def is_curve_tile(tile_type):
        return tile_type.startswith('curve_')

    def get_curve_direction(tile_type):
        return tile_type.split('_')[1]

    def has_left_green_dot(tile_type):
        return 'L' in tile_type

    def has_right_green_dot(tile_type):
        return 'R' in tile_type

    def has_up_green_dot(tile_type):
        return 'U' in tile_type

    def has_down_green_dot(tile_type):
        return 'D' in tile_type

    def is_crossing_tile(tile_type):
        return tile_type.startswith('crossing_')

    def is_within_grid(self, position):
        x,y = position
        if x < 0 or x>= self.size or y<0 or y >= self.size:
            return False
        return True

    def opposite_direction(self, direction):
        if direction == 'up_to_down':
            return 'down_to_up'
        if direction == 'up_to_left':
            return 'left_to_up'
        if direction == 'up_to_right':
            return 'right_to_up'
        if direction == 'down_to_up':
            return 'up_to_down'
        if direction == 'down_to_left':
            return 'left_to_down'
        if direction == 'down_to_right':
            return 'right_to_down'
        if direction == 'left_to_right':
            return 'right_to_left'
        if direction == 'left_to_up':
            return 'up_to_left'
        if direction == 'left_to_down':
            return 'down_to_left'
        if direction == 'right_to_left':
            return 'left_to_right'
        if direction == 'right_to_down':
            return 'down_to_right'
        if direction == 'right_to_up':
            return 'up_to_right'

    def choose_tile(self, possible_tiles):
        return  random.choice(possible_tiles)

    def place_tile(self, position, tile):
        self.grid[position[0]][position[1]] = tile

    def generate(self):
        current_pos = (0, 0)
        self.grid[current_pos[0]][current_pos[1]] = 'down_to_up'
        current_pos = self.get_neighbor_position(current_pos, 'down_to_up')
 
        while True:
            self.check_neighbors(current_pos)
            possible_tiles = self.grid_aux[current_pos[0]][current_pos[1]]
            
            if not possible_tiles:
                break
            print(current_pos)
            print(possible_tiles)
            tile = self.choose_tile(possible_tiles)
            neighbor_x, neighbor_y = self.get_neighbor_position(current_pos, tile)

            if not self.is_within_grid(self.get_neighbor_position(current_pos, tile)) or self.grid[neighbor_x][neighbor_y] is not None:
                tile = self.opposite_direction(tile)
            
            self.place_tile(current_pos, tile)
            print(self.grid)
            current_pos = self.get_neighbor_position(current_pos, tile)
        return self.grid
               
    def check_neighbors(self, position):
        x, y = position
        neighbors = Neighbors()
        # Check neighbors
        if x > 0 and x < self.size-1 and y > 0 and y < self.size-1:
            # All but no edges
            neighbors.down = self.grid[x][y-1]
            neighbors.up = self.grid[x][y+1]
            neighbors.left = self.grid[x-1][y]
            neighbors.right = self.grid[x+1][y]

        if x == 0 and y > 0 and y < self.size-1:
            # Left edge
            neighbors.down = self.grid[x][y-1]
            neighbors.up = self.grid[x][y+1]
            neighbors.left = -1
            neighbors.right = self.grid[x+1][y]   
        
        if y == 0 and x > 0 and x < self.size-1:
            # Bottom edge
            neighbors.down = -1
            neighbors.up = self.grid[x][y+1]
            neighbors.left = self.grid[x-1][y]
            neighbors.right = self.grid[x+1][y]
        
        if y == self.size-1 and x > 0 and x < self.size-1:
            # Top edge
            neighbors.down = self.grid[x][y-1]
            neighbors.up = self.grid[x][y+1]
            neighbors.left = self.grid[x-1][y]
            neighbors.right = self.grid[x+1][y]

        if x == self.size-1 and y > 0 and y < self.size-1:
            # Right edge
            neighbors.down = self.grid[x][y-1]
            neighbors.up = self.grid[x][y+1]
            neighbors.left = self.grid[x][y-1]
            neighbors.right = -1
        
        if x == self.size-1 and y == self.size-1:
            # Top-Right corner
            neighbors.down = self.grid[x][y-1]
            neighbors.up = -1
            neighbors.left = self.grid[x][y-1]
            neighbors.right = -1

        if x == self.size-1 and y == 0:
            # Bottom-right corner
            neighbors.down = -1
            neighbors.up = self.grid[x][y+1]
            neighbors.left = self.grid[x-1][y]
            neighbors.right = -1

        if x == 0 and y == self.size-1:
            # Top-left corner
            neighbors.down = self.grid[x][y-1]
            neighbors.up = -1
            neighbors.left = -1
            neighbors.right = self.grid[x+1][y]
        
        if x == 0 and y == 0:
            # Bottom-left corner
            neighbors.down = -1
            neighbors.up = self.grid[x][y+1]
            neighbors.left = -1
            neighbors.right = self.grid[x+1][y]

        self.grid_aux[x][y] = neighbors.check_compatibility()

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.grid)

# This function doesn't works since backedges
def generate_path():
    size = 6
    grid = [[None for _ in range(size)] for _ in range(size)]
    path = []
    position = (0,0)
    banned_positions = []
    path.append(position)
    n_nodes = random.randint(15,35)
    selected_nodes = 1
    while selected_nodes < n_nodes:
        # Select some random nodes
        banned_position, possible_next_position = get_neighbors(position, path, size, banned_positions)
        if not len(possible_next_position):
            print("No next positions possible")
            return path
        

        position = random.choice(possible_next_position)

        # If is a backedge (crossing with two green dots)
        if position == path[len(path)-1]:
            banned_positions.append(position)
        path.append(position)
        selected_nodes += 1
    return path

def get_neighbors(position, path, size, banned_positions):
    x,y = position
    next_positions = []

    # Check upper
    if (x-1,y) != (0,0) and is_within_grid((x-1, y), size) and (x-1,y) not in banned_positions:
        if path.count((x-1,y)) < 2:
            next_positions.append((x-1,y))
    # Check left
    if (x,y-1) != (0,0) and is_within_grid((x, y-1), size) and (x,y-1) not in banned_positions:
        if path.count((x,y-1)) < 2:
            next_positions.append((x,y-1)) 
    # Check right
    if (x,y+1) != (0,0) and is_within_grid((x, y+1), size) and (x,y+1) not in banned_positions:
        if path.count((x,y+1)) < 2:
            next_positions.append((x,y+1))
    # Check bottom
    if (x+1,y) != (0,0) and is_within_grid((x+1, y), size) and (x+1,y) not in banned_positions:
        if path.count((x+1,y)) < 2:
            next_positions.append((x+1,y))

    next_positions = is_valid_crossing_edge(path, position, next_positions)

    return banned_positions, next_positions

def is_within_grid(position, size):
    x,y = position
    if x < 0 or x>= size or y<0 or y >= size:
        return False
    return True

    
def is_valid_crossing_edge(path, position, next_positions):
    for possible_position in next_positions:
        if possible_position in path:   
            if path.index(position) > 1:
                # Where are we from, before passing for the first time crossing edge
                from_position_bc = path[path.index(position)]
                fpbc_x, fpbc_y = from_position_bc
                x, y = possible_position
                # Check if the crossing is valid
                if y == fpbc_y and x!= fpbc_x:
                    next_positions.remove(possible_position)
            else:
                next_positions.remove(possible_position)
    return next_positions




print(generate_path())







