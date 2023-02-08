# Introdução a ROS 1
ROS (Robot Operating System) é um sistema operacional para robôs que fornece ferramentas para programar, testar e operar robôs. Ele é baseado em módulos que podem ser facilmente integrados para criar aplicações avançadas. Neste guia, você aprenderá sobre os conceitos básicos de tópicos, nós e publicadores/assinantes em ROS.

### Tópicos em ROS
Em ROS, os dados são transmitidos entre módulos através de canais chamados de tópicos. Cada tópico é identificado por um nome único (por exemplo, /cmd_vel) e contém mensagens de um determinado tipo (por exemplo, geometry_msgs/Twist).

### Nós em ROS
Em ROS, cada módulo é conhecido como um nó. Cada nó é responsável por realizar uma tarefa específica, como publicar ou assinar tópicos, processar informações, etc.

### Publicadores e Assinantes em ROS
Em ROS, existem dois tipos de módulos: publicadores e assinantes.

- Publishers: Um publisher é um nó que publica mensagens em um tópico.

- Subscribers: Um subscriber é um nó que se inscreve em um tópico e recebe as mensagens publicadas.
