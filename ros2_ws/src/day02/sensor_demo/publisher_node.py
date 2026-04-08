import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import random

class EnvironmentSensor(Node):

    def __init__(self):
        # Initialize the node with the name 'environment_sensor'
        super().__init__('environment_sensor')

        # Create a publisher that publishes Float32MultiArray messages to the 'environment' topic
        self.publisher_ = self.create_publisher(
            Float32MultiArray,
            '/sensor/environment',
            10
        )

        # Set a timer to call the timer_callback function every 0.5 seconds
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Environment Sensor Node has been started.')

    def timer_callback(self):
        msg = Float32MultiArray()
        # Simulate a temperature reading by generating a random float between 20.0 and 45.0
        temp = round(random.uniform(20.0, 45.0), 2)
        humidity = round(random.uniform(40.0, 90.0), 2)
        msg.data = [temp, humidity]

        self.publisher_.publish(msg)
        self.get_logger().info(f'Temperature: {temp} °C | Humidity: {humidity} %')

def main(args=None):
    rclpy.init(args=args)
    node = EnvironmentSensor()
    rclpy.spin(node) # Keep the node running until it is shut down
    node.destroy_node() # Clean up the node after shutting down
    rclpy.shutdown() # Shut down the ROS client library

if __name__ == '__main__':
    main()
