import random

class Map:
    
    

    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.start_pos = (0, 0)
        self.generate()
        self.DIRECTIONS = [
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

    def get_possible_directions(self, position):
        # Start, we can only choose the straight tile
        if position[0] == 0 and position[1] == 0:
            return self.DIRECTIONS.remove(  'up_to_down',
                                            'down_to_left',
                                            'down_to_right',
                                            'up_to_left',
                                            'up_to_right',
                                            'right_to_left',
                                            'crossing_to_left'
                                            'crossing_to_right',
                                            'crossing_to_down',
                                            'crossing_to_up'
                                        )
        

    def get_next_position(self, position, next_direction):
        if next_direction == 'up_to_down':
        elif next_direction == 'down_to_up':
        elif next_direction == 'down_to_left':
        elif next_direction == 'down_to_right':
        elif next_direction == 'left_to_right':
        elif next_direction == 'right_to_left':
        elif next_direction == 'up_to_left':
        elif next_direction == 'up_to_right':
        elif next_direction == 'crossing_to_left':
        elif next_direction == 'crossing_to_right':
        elif next_direction == 'crossing_to_down':
        elif next_direction == 'crossing_to_up':

    def generate(self):
        current_pos = self.start_pos
        possible_directions = self.get_possible_directions(current_pos)
        # Randomly choose between possible directions
        next_direction = random.choice(possible_directions)
        self.grid[current_pos[0][current_pos[1]]] = next_direction  


        while True:

            



    def generate_(self):
        self.grid[self.start_pos[0]][self.start_pos[1]] = "start"
        current_pos = self.start_pos
        current_direction = random.choice(["up", "down", "left", "right"])
        while True:
            available_pieces = self.get_available_pieces(current_pos, current_direction)
            if not available_pieces:
                break
            next_piece = random.choice(available_pieces)
            if next_piece == "straight":
                piece_directions = ["up", "down", "left", "right"]
                if current_direction in ["up", "down"]:
                    piece_directions.remove("left")
                    piece_directions.remove("right")
                elif current_direction in ["left", "right"]:
                    piece_directions.remove("up")
                    piece_directions.remove("down")
                next_direction = random.choice(piece_directions)
                next_pos = self.get_next_position(current_pos, next_direction)
                if not self.is_within_bounds(next_pos):
                    continue
                if self.grid[next_pos[0]][next_pos[1]]:
                    continue
                self.grid[next_pos[0]][next_pos[1]] = "straight"
                current_pos = next_pos
                current_direction = next_direction
            elif next_piece == "curve_left":
                if current_direction == "up":
                    piece_directions = ["left", "up"]
                elif current_direction == "down":
                    piece_directions = ["right", "down"]
                elif current_direction == "left":
                    piece_directions = ["down", "left"]
                elif current_direction == "right":
                    piece_directions = ["up", "right"]
                next_direction = random.choice(piece_directions)
                next_pos = self.get_next_position(current_pos, next_direction)
                if not self.is_within_bounds(next_pos):
                    continue
                if self.grid[next_pos[0]][next_pos[1]]:
                    continue
                self.grid[next_pos[0]][next_pos[1]] = "curve_left"
                current_pos = next_pos
                current_direction = next_direction
            elif next_piece == "curve_right":
                if current_direction == "up":
                    piece_directions = ["right", "up"]
                elif current_direction == "down":
                    piece_directions = ["left", "down"]
                elif current_direction == "left":
                    piece_directions = ["up", "left"]
                elif current_direction == "right":
                    piece_directions = ["down", "right"]
                next_direction = random.choice(piece_directions)
                next_pos = self.get_next_position(current_pos, next_direction)
                if not self.is_within_bounds(next_pos):
                    continue
                if self.grid[next_pos[0]][next_pos[1]]:
                    continue
                self.grid[next_pos[0]][next_pos[1]] = "curve_right"
                current_pos = next_pos
                current_direction = next_direction
            elif next_piece == "intersection":
                piece_directions = []
                if current_pos[0] > 0 and self.grid[current_pos[0]-1][current_pos[1]]:
                    piece_directions.append("up")
                if current_pos[0] < self.size-1 and self.grid[current_pos[0]+1][current_pos[1]]:
                    piece_directions.append("down")
                if current_pos[1] > 0 and self.grid[current_pos[0]][current_pos[1]-1]:
                    piece_directions.append("left")
                if current_pos[1] < self.size-1 and self.grid[current_pos[0]][current_pos[1]+1]:
                    piece_directions.append("right")
                if not piece_directions:
                    continue
                next_direction = random.choice(piece_directions)
                next_pos = self.get_next_position(current_pos, next_direction)
                if not self.is_within_bounds(next_pos):
                    continue
                if self.grid[next_pos[0]][next_pos[1]]:
                    continue
                self.grid[next_pos[0]][next_pos[1]] = "intersection"
                current_pos = next_pos
                current_direction = self.get_intersection_exit_direction(next_direction)
                self.connect_intersection(current_pos, next_direction, current_direction)

    def get_available_pieces(self, pos, direction):
        available_pieces = []
        if direction in ["up", "down"]:
            if pos[0] > 0 and not self.grid[pos[0]-1][pos[1]]:
                available_pieces.append("straight")
            if pos[0] < self.size-1 and not self.grid[pos[0]+1][pos[1]]:
                available_pieces.append("straight")
            if pos[1] > 0 and not self.grid[pos[0]][pos[1]-1]:
                available_pieces.append("curve_left")
            if pos[1] < self.size-1 and not self.grid[pos[0]][pos[1]+1]:
                available_pieces.append("curve_right")
        elif direction in ["left", "right"]:
            if pos[1] > 0 and not self.grid[pos[0]][pos[1]-1]:
                available_pieces.append("straight")
            if pos[1] < self.size-1 and not self.grid[pos[0]][pos[1]+1]:
                available_pieces.append("straight")
            if pos[0] > 0 and not self.grid[pos[0]-1][pos[1]]:
                available_pieces.append("curve_right")
            if pos[0] < self.size-1 and not self.grid[pos[0]+1][pos[1]]:
                available_pieces.append("curve_left")
        if not available_pieces and self.grid[pos[0]][pos[1]] != "intersection":
            available_pieces.append("intersection")
        return available_pieces

    def get_next_position(self, pos, direction):
        if direction == "up":
            return (pos[0]-1, pos[1])
        elif direction == "down":
            return (pos[0]+1, pos[1])
        elif direction == "left":
            return (pos[0], pos[1]-1)
        elif direction == "right":
            return (pos[0], pos[1]+1)

    def is_within_bounds(self, pos):
        return 0 <= pos[0] < self.size and 0 <= pos[1] < self.size

    def get_intersection_exit_direction(self, entrance_direction):
        exit_directions = {"up": ["left", "right"], "down": ["left", "right"], "left": ["up", "down"], "right": ["up", "down"]}
        return random.choice(exit_directions[entrance_direction])

    def connect_intersection(self, pos, entrance_direction, exit_direction):
        if entrance_direction == "up":
            if pos[0] > 0 and self.grid[pos[0]-1][pos[1]] == "intersection":
                self.grid[pos[0]-1][pos[1]] = exit_direction
            elif pos[0] == 0:
                self.grid[pos[0]][pos[1]] = exit_direction
            elif entrance_direction == "down":
                if pos[0] < self.size-1 and self.grid[pos[0]+1][pos[1]] == "intersection":
                    self.grid[pos[0]+1][pos[1]] = exit_direction
                elif pos[0] == self.size-1:
                    self.grid[pos[0]][pos[1]] = exit_direction
                elif entrance_direction == "left":
                    if pos[1] > 0 and self.grid[pos[0]][pos[1]-1] == "intersection":
                        self.grid[pos[0]][pos[1]-1] = exit_direction
                    elif pos[1] == 0:
                        self.grid[pos[0]][pos[1]] = exit_direction
                    elif entrance_direction == "right":
                        if pos[1] < self.size-1 and self.grid[pos[0]][pos[1]+1] == "intersection":
                            self.grid[pos[0]][pos[1]+1] = exit_direction
                    elif pos[1] == self.size-1:
                        self.grid[pos[0]][pos[1]] = exit_direction

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.grid)

maze = Map(10)
print(maze)