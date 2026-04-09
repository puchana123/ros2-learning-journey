import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

# Warning Thresold for temperature
TEMP_WARNING = 35.0
TEMP_CRITICAL = 40.0
HUM_WARNING = 80.0

class EnvironmentMonitor(Node):

    def __init__(self):
        super().__init__('environment_monitor')

        # Subscribe to the 'environment' topic to receive environment readings
        self.subscription = self.create_subscription(
            Float32MultiArray,
            '/factory/floor1/env', # Subscribe to the remapped topic
            self.listener_callback,
            10
        )
        self.get_logger().info('Environment Monitor Node has been started -- watching /factory/floor1/env topic.')

    def listener_callback(self, msg):
        if len(msg.data) < 2:
            self.get_logger().error('Received data is incomplete. Expected [temperature, humidity].')
            return
        
        temp = round(msg.data[0], 2)
        humidity = round(msg.data[1], 2)

        # Check temperature levels
        if temp >= TEMP_CRITICAL:
            self.get_logger().error(f'CRITICAL: Temperature is {temp} °C! Immediate action required!')
        elif temp >= TEMP_WARNING:
            self.get_logger().warn(f'WARNING: Temperature is {temp} °C! Consider taking action.')
        else:
            self.get_logger().info(f'Temperature is {temp} °C. All is normal.')

        # Check humidity levels
        if humidity >= HUM_WARNING:
            self.get_logger().warn(f'WARNING: Humidity is {humidity} %! Consider taking action.')
        else:
            self.get_logger().info(f'Humidity is {humidity} %. All is normal.')


def main(args=None):
    rclpy.init(args=args)
    node = EnvironmentMonitor()
    rclpy.spin(node) # Keep the node running until it is shut down
    node.destroy_node() # Clean up the node after shutting down
    rclpy.shutdown() # Shut down the ROS client library

if __name__ == '__main__':
    main()