import math
import os
from PIL import Image, ImageDraw
import random
import string
from jinja2 import Template
from Map import generate_path

# CONFIG VARIABLES
NUMBER_GENERATIONS = 1

# Dimensions
TILES_DIR = "Blender Models/"
TILES_TYPE = ["straight.blend", "zig_zag.blend", "curved_90"]
TILES_SIZE = [0.25, 0.25, 0.01]
EVACUATION_ZONE_SIZE = [1.2, 0.9, 0.01]
NUMBER_TILES = random.randint(40,50)
BLACK_LINE_WIDTH = random.uniform(1.0,2.0)
ENUM_TILES_TYPE = {}


WORLD_PATH = "worlds/"


if False:
    # Stupid example to check if it works
    for i in range(NUMBER_GENERATIONS):
        sdf_world_name = 'world_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.sdf'
        
        sdf_model = f"""
            <sdf version="1.7">
                <world name="{sdf_world_name}">
        """
        debug = list()
        pose = [0, 0, 0, 0, 0, 0]

        tile_position = [0][0]

        for j in range(NUMBER_TILES):
            data = {
                "base_tile_number": sdf_world_name + "_" + str(j),
                "pose": " ".join(str(x) for x in pose),
                "tile_number": j,
                "visual_number": "visual_" + str(j),           
                "line_number": "line_" + str(j),
                "line_width": BLACK_LINE_WIDTH/100,
                "direction": "left"
            }

            with open(TILES_DIR + ''.join(random.choice(TILES_TYPE)), 'r') as f:
                template_str = f.read()
            template = Template(template_str)
            output_str = template.render(data)
            sdf_model += output_str
            pose[0] += TILES_SIZE[0]
            
            tile_position[0][0] += 1
        # Remember to add ground_plane
        with open('Gazebo_models/ground_plane.sdf', 'r') as f:
            ground_model = f.read()
        
        sdf_model += ground_model
        sdf_model += f"""
                </world>
            </sdf>
        """
        # Save file
        with open('Gazebo_models/worlds/' + sdf_world_name, 'x') as world:
            world.write(sdf_model)



# TODO: Print in a txt file all infos about the track or even better, create an image of the track

# NOTE: Every sdf world should include at the end the ground_plane, (for the gravity) 
# TODO: Check friction and stuff





def random_compatible_tile(map, position, direction, SIZE=[7,7]):
    """
        :map 
        :position at the beginning should be every time [0,0]
        :direction
        :SIZE optional, indicates the size of the 

        Return a random tile and the position where the tile should be applied compatible with the actual path
    """
def __init__(self):
    self.path = generate_path()
    self.world = []

def generate_model(self):
    model = []
    for _, step in enumerate(self.path):
        x, y = step
        if len(self.path)-1 >= _:
            # Add end tiles (if is not in the limits upsize the grid to fit it)
            pass
            return model
        else:
            # Continue
            next_step = self.path[_+1]
            x_ns, y_ns = next_step

            # check if next step is already checked
            if next_step in self.world:
                pass
            else:
                # Check how many occurency of next step there are
                indexes = [i for i, e in enumerate(self.path) if e == next_step]
                if indexes > 1:
                    # Crossing
                    directions = [0,0,0,0] # up_left, up_right, bottom_left, bottom_right
                    for index in indexes:
                        if len(self.path)-1 >= index:
                            # TODO: In Map.py remove the possibility to end with a cycle
                            # This ends with a cycle, not possible and to be fixed
                            pass
                        else:
                            # Check the direction after the cycle
                            after_cycle = self.path[index+1]
                            x_ac, y_ac = after_cycle
                            # Check the direction before the cycle
                            before_cycle = self.path[index-1]
                            x_bc, y_bc = before_cycle
                            # In case of backedge
                            if  x_bc == x_ac and y == y_ac:
                                # Check the direction of the backedge to rightly fit the green dots
                                if x_bc < x_ns:
                                    # -:|
                                    directions[0] = 1
                                    directions[2] = 1
                                if x_bc > x_ns:
                                    # |:-
                                    directions[1] = 1
                                    directions[3] = 1
                                if y_bc < y_ns:
                                    # .|.
                                    directions[2] = 1
                                    directions[3] = 1
                                if y_bc > y_ns:
                                    # °|°
                                    directions[0] = 1
                                    directions[1] = 1
                            # In case of crossing
                            if x_ns < x_ac:
                                # |-
                                # Check the direction before taking the cycle
                                if y_bc < y_ac:
                                    # |'- 
                                    directions[1] = 1
                                if y_bc > y_ac:
                                    #|.-
                                    directions[3] = 1
                            if x_ns > x_ac:
                                # -|
                                if y_bc < y_ac:
                                    # -'| 
                                    directions[0] = 1
                                if y_bc > y_ac:
                                    # -.|
                                    directions[2] = 1
                        choose_tile(directions)
                else:
                    # Normal tile
                    pass

def choose_tile(directions=None):
    pass