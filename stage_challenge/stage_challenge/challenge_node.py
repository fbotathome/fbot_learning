#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

class ChallengeNode(Node):
    def __init__(self):
        super().__init__('challenge_node')
        self.odom_sub = self.create_subscription(Odometry,'/odom', self.odomCallback,10)
        self.laser_sub = self.create_subscription(LaserScan, 'base_scan', self.laserCallback, 10)

        self.timer = self.create_timer(0.1, self.execute)

    def odomCallback(self, msg):
        '''
        Callback function for odometry data.
        This function is called every time a new odometry message is received.
        From it, you can get the position and orientation of the robot.
        '''
        pass

    def laserCallback(self, msg):
        '''
        Callback function for laser scan data.
        This function is called every time a new laser scan message is received.
        From it, you can get the laser scan data.
        '''
        pass

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
