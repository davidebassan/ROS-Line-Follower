import math
import os
from PIL import Image, ImageDraw
import random
import string
from jinja2 import Template


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

    
    if position[0] == 0 and position[1] == 0:
        return generate_tile('straight.dae'), 


def generate_tile(tile_path, direction):
    """

    """
