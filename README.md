# ROS2 Learning Journey
A collection of ROS2 Humble projects focused on robotics development and automation (IoT/Automation), utilizing Docker as the primary development environment.

## Repository Structure
This workspace consists of two main packages:
1) `sensor_demo`: An environment monitoring system simulation for industrial settings (Temperature + Humidity).
2) `turtle_control`: An open-loop robot motion control system (Square Trajectory).

## Part 1: Sensor Monitoring System (`sensor_demo`)
A simulated multi-sensor data pipeline for factory-floor environment monitoring.

## System Architecture

    [environment_sensor node]
           |
           | topic: /sensor/environment
           | type:  Float32MultiArray [temp, humidity]
           |
    [environment_monitor node]
           |
           +-- NORMAL / WARNING / CRITICAL alerts

## Nodes Configuartion

| Node | Role | Topic |
|------|------|-------|
| environment_sensor | Publisher: sends temp+humidity every 1s | /sensor/environment |
| environment_monitor | Subscriber: threshold-based alerting | /sensor/environment |

## Setup
1) Pull ROS2 image
    ```bash
    docker pull osrf/ros:humble-desktop
2) Connect Volume with Docker container (local files):
    ```bash
   docker run -it --rm -v "${PWD}/ros2_ws:/ros2_ws" osrf/ros:humble-desktop bash
3) Build
    ```bash
    cd /ros2_ws && colcon build
    source install/setup.bash
4) Launch system
    ```bash
    ros2 launch sensor_demo demo.launch.py

## Expected Output

    [environment_sensor]: Temp: 33.21°C  |  Humidity: 72.45%
    [environment_monitor]: [TEMP] NORMAL:   33.21°C
    [environment_monitor]: [HUM]  NORMAL:   72.45%
    [environment_monitor]: [TEMP] WARNING:  37.80°C

## Skills Demonstrated
- Implementation of the ROS 2 Publisher/Subscriber pattern.
- Handling multi-value messages using `Float32MultiArray`.
- Industrial alert logic based on defined thresholds.

## Part 2: Turtlebot Control (`turtle_control`)
Controls the Turtlesim robot to perform a precise square trajectory using a basic State Machine.

Features
- Square Trajectory: Sequential forward movement and 90-degree ($\pi/2$ rad) turns.
- State Machine: Logic-based switching between MOVING and TURNING states.
- Precision Tuning: Fine-tuned ANGULAR_SPEED to compensate for simulation odometry errors.

## Setup & Installation
1) Setup GUI
- Install VcXsrv (X11 server for Windows) from [sourceforge.net](https://sourceforge.net/projects/vcxsrv/).
- Setup docker container with DISPLAY
    ``` bash
    docker run -it --rm -e DISPLAY=host.docker.internal:0.0 -v "${PWD}/ros2_ws:/ros2_ws" osrf/ros:humble-desktop bash
    ```
2) Build
    ``` bash
    cd /ros2_ws && colcon build
    source install/setup.bash
    ```
3) Launch system
    ``` bash
    ros2 launch turtle_control square.launch.py
    ```
## Turtlebot Control demo
<p align="center">
    <img src="assets/turtle_demo.gif" alt="Turtle Square Demo" width="600">
</p>

## Daily note
* Day 1: Installing Docker && Setup ROS2 || ROS Concept.
* Day 2: Create own node (publisher && subscriber) || Docker Local volume.
* Day 3: Create launch file || Upgrade Float32 -> Float32MultiArray (temp+humidity).
* Day 4: Turtlebot control.