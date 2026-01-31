# YASMIN Challenge

**Please make sure you've installed the [turtlesim simulator](https://github.com/butia-bots/butia_learning/tree/main/0-installation#turtlesim) and the YASMIN library before developing this challenge**

This challenge introduces state machines using the [YASMIN](https://github.com/uleroboticsgroup/yasmin) library, a tool used in the team to orchestrate robot behaviors. It assumes you've completed the previous challenges and are comfortable with publishing and subscribing to topics.

The task is to develop a YASMIN state machine that makes the turtle draw an uppercase letter **F** in the turtlesim window.

![turtle](image.png)

## Installing YASMIN

```bash
sudo apt install ros-humble-yasmin ros-humble-yasmin-ros
```

If the packages are not available via apt, you can build from source:

```bash
cd fbot_ws/src
git clone https://github.com/uleroboticsgroup/yasmin.git
cd ..
colcon build --symlink-install
```

## How to develop the challenge

The challenge provides a state machine skeleton with two states:

- **MOVE**: Publishes Twist messages on `/turtle1/cmd_vel` to move the turtle forward. 
- **ROTATE**: Publishes Twist messages to rotate the turtle.

You should first create the states as you think they should function and then implement the logic to make the turtle draw the letter F through the state machine logic defined in the main function.

Then run the simulator:

```bash
cd fbot_ws
source install/setup.bash
ros2 run turtlesim turtlesim_node
```

And the node:

```bash
ros2 run yasmin_challenge challenge_node
```

## Concepts

- **State**: A class that inherits from `yasmin.State` and implements `execute(blackboard)`. It must return one of its declared outcomes.
- **StateMachine**: A container that holds states and defines transitions between them based on outcomes.
- **Blackboard**: A shared dictionary that states use to pass data to each other (e.g., the turtle's position).
- **Outcomes**: Strings like `SUCCEED`, `ABORT`, `CANCEL` that determine which transition to follow.

## Help

If you have specific questions, feel free to open a [discussion](https://github.com/butia-bots/butia_learning/discussions) in this repository.

---

## Credits

Made and maintained by [Gabriel Dorneles](https://github.com/gadorneles)
