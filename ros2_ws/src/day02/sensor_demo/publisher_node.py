import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TemperatureSensor(Node):

    def __init__(self):
        # Initialize the node with the name 'temperature_sensor'
        super().__init__('temperature_sensor')

        # Create a publisher that publishes Float32 messages to the 'temperature' topic
        self.publisher_ = self.create_publisher(
            Float32,
            '/sensor/temp',
            10
        )

        # Set a timer to call the timer_callback function every 0.5 seconds
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info('Temperature Sensor Node has been started.')

    def timer_callback(self):
        msg = Float32()
        # Simulate a temperature reading by generating a random float between 20.0 and 45.0
        msg.data = round(random.uniform(20.0, 45.0), 2)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published temperature: {msg.data} °C')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensor()
    rclpy.spin(node) # Keep the node running until it is shut down
    node.destroy_node() # Clean up the node after shutting down
    rclpy.shutdown() # Shut down the ROS client library

if __name__ == '__main__':
    main()
