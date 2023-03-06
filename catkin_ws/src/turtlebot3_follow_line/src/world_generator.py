import math
import os
from PIL import Image, ImageDraw

# Dimensioni della piastrella in metri
PIECE_SIZE = 0.02

# Definizione del percorso del file dell'immagine piastrella
TILE_IMAGE_PATH = os.path.join(os.getcwd(), 'tile.png')

# Generazione dell'immagine della piastrella
tile_image = Image.new('RGB', (int(PIECE_SIZE*100), int(PIECE_SIZE*100)), (255, 255, 255))
draw = ImageDraw.Draw(tile_image)
draw.line((0, int(PIECE_SIZE*50), int(PIECE_SIZE*100), int(PIECE_SIZE*50)), fill=(0, 0, 0), width=2)

# Salvataggio dell'immagine piastrella
tile_image.save(TILE_IMAGE_PATH)

# Generazione del modello SDF
world = f'''<?xml version="1.0"?>
<sdf version="1.5">
  <model name="tile">
    <static>true</static>
    <link name="link">
      <collision name="collision">
        <geometry>
          <box>
            <size>{PIECE_SIZE} {PIECE_SIZE} 0.001</size>
          </box>
        </geometry>
      </collision>
      <visual name="visual">
        <geometry>
          <plane>
            <normal>0 0 1</normal>
            <size>{PIECE_SIZE} {PIECE_SIZE}</size>
          </plane>
        </geometry>
        <material>
          <lighting>1</lighting>
          <script>
            <uri>file://media/materials/scripts/gazebo.material</uri>
            <name>Gazebo/White</name>
          </script>
        </material>
      </visual>
    </link>
  </model>
</sdf>'''

# Creazione del file SDF del modello piastrella
with open('tile.model', 'w') as f:
    f.write(world)
