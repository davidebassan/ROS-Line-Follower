# ROS Noetic Container For Docker
**DISCLAIM**: Image for arm64 (Apple Silicon), check docker hub to find your version and change in the Dockerfile the first line

| Arc  | Instruction |
| --- | --- |
| amd64 | FROM dorowu/ubuntu-desktop-lxde-vnc:focal |


1. docker-compose up (for the first time use --build)
2. connect to localhost:6080

From now you can start to use ROS on your docker container

### Important
You should use sudo only if is strictly necessary. 

### Common Issues
- During catkin_init_workspace or catkin_make [Errno13] Permission Denied.
In this case, check if the folder in which you want to init your project have the right privilegies, (ls -ld .)
If not, sudo chmod -R a+rwx in the right folder
