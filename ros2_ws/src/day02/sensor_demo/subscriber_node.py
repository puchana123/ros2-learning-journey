import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

# Warning Thresold for temperature
TEMP_WARNING = 35.0
TEMP_CRITICAL = 40.0

class TemperatureMonitor(Node):

    def __init__(self):
        super().__init__('temperature_monitor')

        # Subscribe to the 'temperature' topic to receive temperature readings
        self.subscription = self.create_subscription(
            Float32,
            '/sensor/temp',
            self.listener_callback,
            10
        )
        self.get_logger().info('Temperature Monitor Node has been started -- watching /sensor/temp topic.')

    def listener_callback(self, msg):
        temp = round(msg.data, 2)

        if temp >= TEMP_CRITICAL:
            self.get_logger().error(f'CRITICAL: Temperature is {temp} °C! Immediate action required!')
        elif temp >= TEMP_WARNING:
            self.get_logger().warn(f'WARNING: Temperature is {temp} °C! Consider taking action.')
        else:
            self.get_logger().info(f'Temperature is {temp} °C. All is normal.')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureMonitor()
    rclpy.spin(node) # Keep the node running until it is shut down
    node.destroy_node() # Clean up the node after shutting down
    rclpy.shutdown() # Shut down the ROS client library

if __name__ == '__main__':
    main()