import os

# Dimensioni dell'area di evacuazione
evacuation_zone_width = 1.2  # in metri
evacuation_zone_length = 0.9  # in metri
wall_height = 0.1  # in metri

# Dimensioni delle porte
door_width = 0.25  # in metri
door_height = wall_height  # in metri
door_strip_width = 0.025  # in metri

# Posizione delle porte sull'asse x (in metri)
door1_x = 0.2
door2_x = 1.0

# Posizione delle porte sull'asse y (in metri)
door1_y = 0.0
door2_y = 0.9

# Genera il file del modello dell'area di evacuazione
model_name = "evacuation_zone.sdf"
sdf_file_path = "Gazebo_models"
os.makedirs(sdf_file_path, exist_ok=True)

model_sdf = f'''
<?xml version="1.0"?>
<sdf version="1.5">
  <model name="{model_name}">
    <link name="base_link">
      <collision name="collision">
        <geometry>
          <box>
            <size>{evacuation_zone_width} {evacuation_zone_length} {wall_height}</size>
          </box>
        </geometry>
        <pose>0 0 0 0 0 0</pose>
      </collision>
      <visual name="visual">
        <geometry>
          <box>
            <size>{evacuation_zone_width} {evacuation_zone_length} {wall_height}</size>
          </box>
        </geometry>
        <material>
          <script>
            <name>Gazebo/White</name>
            <uri>file://media/materials/scripts/gazebo.material</uri>
          </script>
          <shader type="pixel"/>
        </material>
        <pose>0 0 0 0 0 0</pose>
      </visual>
    </link>

    <link name="door1">
      <collision name="collision">
        <geometry>
          <box>
            <size>{door_width} {door_height} {wall_height}</size>
          </box>
        </geometry>
        <pose>{door1_x} {door1_y} {wall_height/2} 0 0 0</pose>
      </collision>
      <visual name="visual">
        <geometry>
          <box>
            <size>{door_width} {door_height} {wall_height}</size>
          </box>
        </geometry>
        <material>
          <script>
            <name>Gazebo/Grey</name>
            <uri>file://media/materials/scripts/gazebo.material</uri>
          </script>
          <shader type="pixel"/>
        </material>
        <pose>{door1_x} {door1_y} {wall_height/2} 0 0 0</pose>
      </visual>
    </link>
    <link name="door2">
      <collision name="collision">
        <geometry>
        <box>
            <size>{door_width} {door_height} {wall_height}</size>
        </box>
        </geometry>
        <pose>{door2_x} {door2_y} {wall_height/2} 0 0 0</pose>
      </collision>
      <visual name="visual">
        <geometry>
        <box>
          <size>{door_width} {door_height} {wall_height}</size>
        </box>
        </geometry>
        <material>
        <script>
          <name>Gazebo/Black</name>
          <uri>file://media/materials/scripts/gazebo.material</uri>
        </script>
        <shader type="pixel"/>
        </material>
        <pose>{door2_x} {door2_y} {wall_height/2} 0 0 0</pose>
      </visual>
    </link>

    <link name="door_strip1">
      <collision name="collision">
        <geometry>
          <box>
            <size>{door_strip_width} {door_height} {wall_height}</size>
          </box>
        </geometry>
        <pose>{door1_x+(door_width/2)-(door_strip_width/2)} {door1_y} {wall_height/2} 0 0 0</pose>
      </collision>
      <visual name="visual">
        <geometry>
          <box>
            <size>{door_strip_width} {door_height} {wall_height}</size>
          </box>
        </geometry>
        <material>
          <script>
            <name>Gazebo/Silver</name>
            <uri>file://media/materials/scripts/gazebo.material</uri>
          </script>
          <shader type="pixel"/>
        </material>
        <pose>{door1_x+(door_width/2)-(door_strip_width/2)} {door1_y} {wall_height/2} 0 0 0</pose>
      </visual>
    </link>

    <link name="door_strip2">
      <collision name="collision">
        <geometry>
          <box>
            <size>{door_strip_width} {door_height} {wall_height}</size>
          </box>
        </geometry>
        <pose>{door2_x+(door_width/2)-(door_strip_width/2)} {door2_y} {wall_height/2} 0 0 0</pose>
      </collision>
      <visual name="visual">
        <geometry>
          <box>
            <size>{door_strip_width} {door_height} {wall_height}</size>
          </box>
        </geometry>
        <material>
          <script>
            <name>Gazebo/Black</name>
            <uri>file://media/materials/scripts/gazebo.material</uri>
          </script>
          <shader type="pixel"/>
        </material>
        <pose>{door2_x+(door_width/2)-(door_strip_width/2)} {door2_y} {wall_height/2} 0 0 0</pose>
      </visual>
    </link>
  </model>
'''

with open(sdf_file_path+"/"+model_name,'w') as f:
    f.write(model_sdf)