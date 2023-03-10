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
                'left_to_down'
                'right_to_left',
                'right_to_down',
                'right_to_up',
                'crossing_to_left',
                'crossing_to_right',
                'crossing_to_down', 
                'crossing_to_up']
            
        def check_compatibility(self):
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

            elif self.up in ['up_to_down','down_to_up', 'down_to_left', 'left_to_down', 'right_to_down', 'down_to_right', 'crossing_to_left', 'crossing_to_right', 'crossing_to_down', 'crossing_to_up']:
                to_remove = [
                    'left_to_right',
                    'right_to_left',
                    'up_to_left',
                    'up_to_right',
                    'left_to_up',
                    'right_to_up'
                ]
            
                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            elif self.up in ['up_to_left', 'up_to_right', 'left_to_up', 'right_to_up','right_to_left', 'left_to_right']:
                to_remove = [
                    'up_to_down',
                    'down_to_up'
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

            elif self.down in ['up_to_down', 'down_to_up', 'left_to_up', 'up_to_left', 'right_to_up', 'up_to_right', 'crossing_to_left', 'crossing_to_right', 'crossing_to_down', 'crossing_to_up']:
                to_remove = [
                    'left_to_right',
                    'right_to_left',
                    'left_to_down',
                    'down_to_left',
                    'down_to_right',
                    'right_to_down'
                ]

                for x in to_remove:
                    if x in compatible_tiles:
                        compatible_tiles.remove(x)

            elif self.down in ['left_to_down', 'down_to_left', 'down_to_right', 'right_to_down', 'left_to_right', 'right_to_left']:
                to_remove = [
                    'up_to_down', 
                    'down_to_up', 
                    'left_to_up', 
                    'up_to_left', 
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
                    'crossing_to_up']


    def update_possible_tiles(self, position, possible_tiles):
        row, col = position
        size = len(self.grid)
        for d in self.DIRECTIONS:
            neighbor_row, neighbor_col = self.get_neighbor_position(position, d)
            if (0 <= neighbor_row < size) and (0 <= neighbor_col < size):
                neighbor_tile = self.grid[neighbor_row][neighbor_col]
                possible_tiles[(neighbor_row, neighbor_col)] = self.get_possible_directions((neighbor_row, neighbor_col), self.grid)
        return possible_tiles

    def get_neighbor_position(self, position, direction):
        # TODO: Da sistemare
        row, col = position
        if direction == 'up_to_down':
            return row + 1, col
        elif direction == 'down_to_up':
            return row - 1, col
        elif direction == 'down_to_left':
            return row, col - 1
        elif direction == 'down_to_right':
            return row, col + 1
        elif direction == 'left_to_right':
            return row, col + 1
        elif direction == 'right_to_left':
            return row, col - 1
        elif direction == 'up_to_left':
            return row - 1, col
        elif direction == 'up_to_right':
            return row - 1, col
        elif direction == 'crossing_to_left':
            return row, col - 1
        elif direction == 'crossing_to_right':
            return row, col + 1
        elif direction == 'crossing_to_down':
            return row + 1, col
        elif direction == 'crossing_to_up':
            return row - 1, col
        else:
            raise ValueError("Invalid direction provided.")

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

    def is_within_grid(position, grid):
        rows, cols = len(grid), len(grid[0])
        return 0 <= position[0] < rows and 0 <= position[1] < cols

    def opposite_direction(direction):
        if direction == 'up':
            return 'down'
        elif direction == 'down':
            return 'up'
        elif direction == 'left':
            return 'right'
        elif direction == 'right':
            return 'left'

    def choose_tile(self, possible_tiles):
        return  random.choice(possible_tiles)


    def place_tile(self, position, tile):
        self.grid[position[0]][position[1]] = tile

    def generate(self):
        current_pos = (0, 0)
        while True:
            self.check_neighbors(current_pos)
            possible_tiles = self.grid_aux[current_pos[0]][current_pos[1]]
            if not possible_tiles:
                break
            tile = self.choose_tile(possible_tiles)
            self.place_tile(current_pos, tile)
            current_pos = self.get_neighbor_position(current_pos, tile)
        return self.grid

    def generate_neighbors_map(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.check_neighbors((i, j))
               
    def check_neighbors(self, position):
        x, y = position
        possible_tiles = [
                  'up_to_down',
                  'down_to_up',
                  'down_to_left',
                  'down_to_right',
                  'left_to_right',
                  'right_to_left',
                  'up_to_left',
                  'up_to_right',
                  'crossing_to_left',
                  'crossing_to_right',
                  'crossing_to_down', 
                  'crossing_to_up']
        
        neighbors = []


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

maze = Map(10)
print(maze)
