## ROS2 Sensor Demo - Environment Monitoring System
A ROS2 Humble demonstration of a multi-sensor data pipeline
simulating factory-floor environment monitoring (temperature + humidity).

## System Architecture

    [environment_sensor node]
           |
           | topic: /sensor/environment
           | type:  Float32MultiArray [temp, humidity]
           |
    [environment_monitor node]
           |
           +-- NORMAL / WARNING / CRITICAL alerts

## Nodes

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
- ROS2 Humble Publisher / Subscriber pattern
- Float32MultiArray multi-value message
- Launch file for multi-node system
- Threshold-based industrial alert logic

## Daily note
* Day 1: Installing Docker && Setup ROS2 || ROS Concept
* Day 2: Create own node (publisher && subscriber) || Docker Local volume
* Day 3: Create launch file || Upgrade Float32 -> Float32MultiArray (temp+humidity)