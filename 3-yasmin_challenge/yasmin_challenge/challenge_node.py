#!/usr/bin/env python3

import rclpy
import yasmin
import time
import math

from yasmin import State, StateMachine, Blackboard
from yasmin_ros.basic_outcomes import SUCCEED, ABORT, CANCEL
from yasmin_ros.yasmin_node import YasminNode
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

MOVE = "move"
ROTATE = "rotate"


class MoveState(State):
    def __init__(self):
        super().__init__(outcomes=[SUCCEED, ABORT, CANCEL])
        self.node = YasminNode.get_instance()
        self.vel_publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose = None
        self.pose_sub = self.node.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

    def pose_callback(self, msg):
        self.pose = msg

    def execute(self, blackboard: Blackboard) -> str:
        '''
        Move the turtle forward by a distance.
        Use the turtle's pose (subscribe to /turtle1/pose) to know when you've traveled enough.
        '''
        # Implement your logic here 
        pass


class RotateState(State):
    def __init__(self):
        super().__init__(outcomes=[SUCCEED, ABORT, CANCEL])
        self.node = YasminNode.get_instance()
        self.vel_publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose = None
        self.pose_sub = self.node.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

    def pose_callback(self, msg):
        self.pose = msg

    def execute(self, blackboard: Blackboard) -> str:
        '''
        Rotate the turtle by the angle (in radians).
        Positive = counterclockwise, negative = clockwise.
        Use the turtle's pose to know when you've rotated enough.
        '''
        pass


def main(args=None):
    rclpy.init(args=args)

    blackboard = Blackboard()

    sm = StateMachine(outcomes=[SUCCEED, ABORT, CANCEL])

    sm.add_state("MOVE", MoveState(), transitions={
        SUCCEED: SUCCEED,
        ABORT: ABORT,
        CANCEL: CANCEL,
    })

    sm.add_state("ROTATE", RotateState(), transitions={
        SUCCEED: SUCCEED,
        ABORT: ABORT,
        CANCEL: CANCEL,
    })

    # Add more states and fix the transitions to make the turtle draw the letter F

    try:
        outcome = sm(blackboard)
        yasmin.YASMIN_LOG_INFO(f"State machine finished with outcome: {outcome}")
    except KeyboardInterrupt:
        if sm.is_running():
            sm.cancel_state()

    if rclpy.ok():
        rclpy.shutdown()


if __name__ == '__main__':
    main()
