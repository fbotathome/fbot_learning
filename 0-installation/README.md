# Section 0 - Installation / Seção 0 - Instalação

## English

### ROS2

For these tutorials, you must have ROS2 Humble installed on an Ubuntu 22.04 system. For the ROS2 installation please follow this [step-by-step guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html).

### Turtlesim

- For the first challenge, you'll need to download the turtlesim ROS2 packages:

```bash
sudo apt update
sudo apt install ros-humble-turtlesim
```

- If it was installed correctly, you should be able to launch the simulation:

```bash
ros2 run turtlesim turtlesim_node
```

### Stage Simulator

- For the second challenge, you'll need to download the Stage simulator ROS2 packages:

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

---

## Português

### ROS2

Para estes tutoriais, você precisa ter o ROS2 Humble instalado em um sistema Ubuntu 22.04. Para a instalação do ROS2, siga este [guia passo a passo](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html).

### Turtlesim

- Para o primeiro desafio, você precisará baixar os pacotes ROS2 do turtlesim:

```bash
sudo apt update
sudo apt install ros-humble-turtlesim
```

- Se foi instalado corretamente, você deve conseguir iniciar a simulação:

```bash
ros2 run turtlesim turtlesim_node
```

### Stage Simulator

- Para o segundo desafio, você precisará baixar os pacotes ROS2 do Stage simulator:

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

- Se foi instalado corretamente, você deve conseguir iniciar a simulação:

```bash
cd fbot_ws
source install/setup.bash
ros2 launch stage_ros2 stage.launch.py world:=cave enforce_prefixes:=false one_tf_tree:=true
```
