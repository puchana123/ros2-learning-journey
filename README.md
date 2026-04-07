# ROS2 Learning
ROS2 Humble with Docker Learning Progress

## Setup
1) Connect Volume with Docker (local files):
    ```bash
   docker run -it --rm -v "${PWD}/ros2_ws:/ros2_ws" osrf/ros:humble-desktop bash
2) Build
    ```bash
    cd /ros2_ws && colcon build
3) Run Node
    ```bash
    source install/setup.bash
    ros2 run sensor_demo publisher_node

## Daily note
* Day 1: Installing Docker && Setup ROS2 || ROS Concept
* Day 2: Create own node (publisher && subscriber) || Docker Local volume