# Stage Challenge

This challenge is meant to introduce some basic ROS concepts to new users, however it assumes you’re familiar with fundamental ROS concepts, including creating and building packages and running nodes.

The task is to develop a ROS node to control a differential robot. The node must be capable of guiding the robot from the origin (x=-7.0, y=-7.0) to the target coordinates (x=4.5, y=4.0) while avoiding obstacles. The minimum distance error from the robot to the target in relation to x and y is 0.4.

![stage simulator](image.png)

The robot and LiDAR are visible in the bottom-left corner of the screen, while the target is highlighted in green at the top-right.

## Installation

- For this challenge, you'll need to download the Stage simulator ROS2 packages:

```bash
sudo apt-get install git cmake g++ libjpeg8-dev libpng-dev libglu1-mesa-dev libltdl-dev libfltk1.1-dev
```

```bash
mkdir fbot_ws
cd fbot_ws
mkdir src
cd src
git clone https://github.com/tuw-robotics/Stage
git clone https://github.com/tuw-robotics/stage_ros2
cd ...
colcon build --symlink-install --cmake-args -DOpenGL_GL_PREFERENCE=LEGACY
```

- If it was installed correctly, you should be able to launch the simulation:

```bash
cd fbot_ws
source install/setup.bash
ros2 launch stage_ros2 stage.launch.py world:=cave enforce_prefixes:=false one_tf_tree:=true
``` 

- The robot in the simulation will be publishing a bunch of topics inside the ROS system, most importantly:

    - [Odometry:](https://docs.ros2.org/foxy/api/nav_msgs/msg/Odometry.html) This represents an estimate of the robot's position and velocity in free space.
    - [LaserScan:](https://docs.ros2.org/foxy/api/sensor_msgs/msg/LaserScan.html) Supplies range measurements from a 2D planar laser scanner, useful for obstacle detection and mapping the environment.

- The odometry data will be utilized to track the robot’s current pose (position and orientation) on the 2D plane. The laser scan data will be used to identify nearby obstacles.

## How to develop the challenge

You must use the robot’s position, which starts at the initial coordinates (x = -7.0, y = -7.0), provided by the /ground_truth topic, along with the distance information captured by the laser, which is published to the /base_scan topic. The robot should be controlled by sending messages to the /cmd_vel topic, which contains the robot’s linear and angular velocities. The velocity control can be handled in either a discrete or continuous manner, with discretization being an easier approach for implementing the control algorithm.

To implement this behavior, you should modify the execute() method of the ChallengeNode node provided in this repository. Then run the node:

```bash
ros2 run stage_challenge challenge_node
```


## Laser Sensor

The laser sensor performs 1080 measurements and covers 270 degrees (from 0 to 270 degrees), with 135 degrees to the left (counterclockwise) and 135 degrees to the right (clockwise), corresponding to the blue and green lines in the figure below. In the LaserScan message, the ranges vector stores the distance values for each measurement, where the first elements represent measurements to the right, and the last elements represent measurements to the left, as indicated by the red lines in the figure.

![Laser sensor](laserscan_image.png)

## Credits

Made and mantained by [Gabriel Dorneles](https://github.com/gadorneles) \
Based on the work of [Ricardo Grando](https://github.com/ricardoGrando)