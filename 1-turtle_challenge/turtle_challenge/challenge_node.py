#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ChallengeNode(Node):
    def __init__(self):
        super().__init__('challenge_node')

        self.vel_pubslisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.execute)

    def execute(self):
        '''
        This function is called periodically by the timer.
        It is responsible for controlling the robot's movement.
        It should publish a Twist message to the /cmd_vel topic to control the robot.
        ''' 
        # Here you can implement your control logic
        pass


def main(args=None):
    rclpy.init(args=args)
    node = ChallengeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
