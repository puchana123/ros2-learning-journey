import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# -- Variables globales --
LINEAR_SPEED = 2.0  # Walk speed (units/s)
ANGULAR_SPEED = 1.565 # Turn speed (rad/s)
MOVE_TIME = 2.0  # Time for each movement (s)
TURN_TIME = 1.0 # Time for each turn (s)
REPEAT = 1 # Number of times to repeat the walk-turn sequence

class SquareController(Node):

    def __init__(self):
        super().__init__('square_controller')
        self.publisher_ = self.create_publisher(
            Twist, 
            'turtle1/cmd_vel', 
            10
        )
        self.state = 'MOVING' # Start in the moving state
        self.state_timer = 0.0
        self.sides_done = 0
        self.laps_done = 0

        # timer to control the movement and turning
        self.timer = self.create_timer(0.01, self.control_loop) # 100 Hz
        self.get_logger().info(
            f'Square controller started - {REPEAT} laps'
        )

    def control_loop(self):
        # Stop the turtle after completing the laps
        if self.laps_done >= REPEAT:
            self.stop()
            self.get_logger().info('Completed all laps. Stopping turtle.')
            self.timer.cancel() # Stop the timer to end the control loop
            return
        
        msg = Twist()
        self.state_timer += 0.01

        if self.state == 'MOVING':
            msg.linear.x = LINEAR_SPEED
            msg.angular.z = 0.0
            self.publisher_.publish(msg)

            if self.state_timer >= MOVE_TIME:
                self.state = 'TURNING'
                self.state_timer = 0.0
                self.get_logger().info(f'Moving completed for side {self.sides_done + 1} - starting turn')

        elif self.state == 'TURNING':
            msg.linear.x = 0.0
            msg.angular.z = ANGULAR_SPEED
            self.publisher_.publish(msg)

            if self.state_timer >= TURN_TIME:
                self.state = 'MOVING'
                self.state_timer = 0.0
                self.sides_done += 1

                if self.sides_done >= 4: # Completed a lap (4 sides)
                    self.sides_done = 0
                    self.laps_done += 1
                    self.get_logger().info(f'Lap {self.laps_done} completed')

    def stop(self):
        # Publish Twist() to stop the turtle
        msg = Twist()
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SquareController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()