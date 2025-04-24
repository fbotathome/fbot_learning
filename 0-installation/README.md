# Section 0 - Installation

## ROS2

For these tutorials, you must have ROS2 Humble installed on an Ubuntu 22.04 system. For the ROS2 installation please folow this [step-by-step guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html).

## Stage Simulator

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
