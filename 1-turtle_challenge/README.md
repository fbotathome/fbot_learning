# Turtle Challenge

## English

**Please make sure you've installed the [turtle sim simulator](https://github.com/butia-bots/butia_learning/tree/main/0-installation#turtlesim) before developing this challenge**

This challenge is meant to introduce some basic ROS concepts to new users, however it assumes you're familiar with fundamental ROS concepts, including creating and building packages and running nodes.

The task is to develop a ROS node to control a turtle. The node must be capable of guiding the turtle to form a square in the turtlesim simulator.

![turtle](image.png)


### How to develop the challenge

The challenge node should publish [Twist](https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Twist.html) messages in the /turtle1/cmd_vel topic in order to make the turtle form a square.

To implement this behavior, you should modify the execute() method of the ChallengeNode node provided in this repository. Then run the simulator:

```bash
cd fbot_ws
source install/setup.bash
ros2 run turtlesim turtlesim_node
```

And the node:

```bash
ros2 run turtle_challenge challenge_node
```

### Help

If you have specific questions, feel free to open a [discussion](https://github.com/butia-bots/butia_learning/discussions) in this repository.

---

## Português

**Certifique-se de ter instalado o [simulador turtlesim](https://github.com/butia-bots/butia_learning/tree/main/0-installation#turtlesim) antes de desenvolver este desafio**

Este desafio tem como objetivo introduzir alguns conceitos básicos de ROS para novos usuários, porém assume que você já está familiarizado com conceitos fundamentais de ROS, incluindo criar e compilar packages e executar nodes.

A tarefa é desenvolver um node ROS para controlar uma tartaruga. O node deve ser capaz de guiar a tartaruga para formar um quadrado no simulador turtlesim.

![turtle](image.png)


### Como desenvolver o desafio

O node do desafio deve publicar mensagens [Twist](https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Twist.html) no topic /turtle1/cmd_vel para fazer a tartaruga formar um quadrado.

Para implementar esse comportamento, você deve modificar o método execute() do node ChallengeNode fornecido neste repositório. Então execute o simulador:

```bash
cd fbot_ws
source install/setup.bash
ros2 run turtlesim turtlesim_node
```

E o node:

```bash
ros2 run turtle_challenge challenge_node
```

### Ajuda

Se você tiver dúvidas específicas, fique à vontade para abrir uma [discussion](https://github.com/butia-bots/butia_learning/discussions) neste repositório.

---

## Credits / Créditos

Made and maintained by [Gabriel Dorneles](https://github.com/gadorneles)
