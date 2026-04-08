from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Create a LaunchDescription object to hold the nodes we want to launch
    publisher = Node(
        package='sensor_demo',
        executable='publisher_node',
        name='environment_sensor',
        output='screen', # Print output to the console
        remappings=[
            ('/sensor/environment', '/factory/floor1/env') # Remap the topic if needed
        ]
    )

    subscriber = Node(
        package='sensor_demo',
        executable='subscriber_node',
        name='environment_monitor',
        output='screen'
    )

    return LaunchDescription([publisher, subscriber]) # Return the LaunchDescription object