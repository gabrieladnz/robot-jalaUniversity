# -*- coding: utf-8 -*-
"""Robo 2.0 Jala(grupo1)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-J7Zf0kFFJIQ4DRPFrHmmZcJb1FrmZRy
"""

class Part():

    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption

    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption,
        }

    def reduce_edefense(self, attack_level):
        self.defense_level = self.defense_level - attack_level
        if self.defense_level <= 0:
            self.defense_level = 0 

    def is_available(self):
        return self.defense_level <= 0


class Robot:
    def __init__(self, name, color_code, selected_robot):
        self.name = name
        self.color_code = color_code
        self.selected_robot = selected_robot
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15,
                 defense_level=0, energy_consumption=10),
            Part("Left Arm", attack_level=3,
                 defense_level=20, energy_consumption=10),
            Part("Right Arm", attack_level=6,
                 defense_level=20, energy_consumption=10),
            Part("Left Leg", attack_level=4,
                 defense_level=20, energy_consumption=15),
            Part("Right Leg", attack_level=8,
                 defense_level=20, energy_consumption=15),
        ]



    def print_status(self):
        print(self.color_code)
        str_robot = self.selected_robot.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["preto"])

    def greet(self):
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print("Olá! Meu nome é", self.name)

    def print_energy(self):
        print("Nós temos", self.energy,"% de energia sobrando")

    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

    def is_there_available_part(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

    def is_on(self):
        return self.energy >= 0

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        attack_level = self.parts[part_to_use].attack_level
        defense_level = enemy_robot.parts[part_to_attack].defense_level

        if attack_level > defense_level:
            damage = attack_level - defense_level
        else:
            damage = 0

        enemy_robot.parts[part_to_attack].reduce_edefense(attack_level)

        self.energy -= self.parts[part_to_use].energy_consumption
        enemy_robot.energy -= damage

        if self.energy < 0:
            self.energy = 0

robot_origen = r"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
       0: {head_name}
       Is available: {head_status}
       Attack: {head_attack}                              
       Defense: {head_defense}
       Energy consumption: {head_energy_consump}
               ^
               |                  |1: {weapon_name}
               |                  |Is available: {weapon_status}
      ____     |    ____          |Attack: {weapon_attack}
     |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
     |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
     |oooo|/\_||_/\|oooo|          
     `----' / __ \  `----'           |2: {left_arm_name}
    '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
    /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
   / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
  |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
  <_>      |=\__/=|      <_> ------> |
  <_>      |------|      <_>         |3: {right_arm_name}
  | |   ___|======|___   | |         |Is available: {right_arm_status}
 // \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
 |  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
 |\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
 \__/  _|||        |||_  \__/        
       | ||        || |          |4: {left_leg_name} 
      [==|]        [|==]         |Is available: {left_leg_status}
      [===]        [===]         |Attack: {left_leg_attack}
       >_<          >_<          |Defense: {left_leg_defense}
      || ||        || ||         |Energy consumption: {left_leg_energy_consump}
      || ||        || || ------> |
      || ||        || ||         |5: {right_leg_name}
    __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
   /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                 |Defense: {right_leg_defense}
                                 |Energy consumption: {right_leg_energy_consump}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 """

robot_ultron = r'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
           0: {head_name}
           Is available: {head_status}
           Attack: {head_attack}                              
           Defense: {head_defense}
           Energy consumption: {head_energy_consump}
                           ^
                           |                       |1: {weapon_name}
                          ___                      |Is available: {weapon_status}
                         /[-])//  ___              |Attack: {weapon_attack}
                    __ --\ `_/~--|  / \            |Defense: {weapon_defense}
                  /_-/~~--~~ /~~~\\_\ /\           |Energy consumption: {weapon_energy_consump}
                  |  |___|===|_-- | \ \ \        
_/~~~~~~~~|~~\,   ---|---\___/----|  \/\-\             |2: {left_arm_name}
~\________|__/   / // \__ |  ||  / | |   | |           |Is available: {left_arm_status}
         ,~-|~~~~~\--, | \|--|/~|||  |   | |           |Attack: {left_arm_attack}
         [3-|____---~~ _--'==;/ _,   |   |_|           |Defense: {left_arm_defense}
                     /   /\__|_/  \  \__/--/           |Energy consumption: {left_arm_energy_consump}
                    /---/_\  -___/ |  /,--|    ------> |
                    /  /\/~--|   | |  \///             |3: {right_arm_name}
                   /  / |-__ \    |/                   |Is available: {right_arm_status}
                  |--/ /      |-- | \                  |Attack: {right_arm_attack}
                 \^~~\\/\      \   \/- _               |Defense: {right_arm_defense}
                  \    |  \     |~~\~~| \              |Energy consumption: {right_arm_energy_consump}
                   \    \  \     \   \  | \      
                     \    \ |     \   \    \              |4: {left_leg_name} 
                       |~~|\/\|     \   \   |             |Is available: {left_leg_status}
                     |   |/         \_--_- |\             |Attack: {left_leg_attack}
                     |  /            /   |/\/             |Defense: {left_leg_defense}
                      ~~             /  /                 |Energy consumption: {left_leg_energy_consump}
                                    |__/          ------> |
                                                          |5: {right_leg_name}
                                                          |Is available: {right_leg_status}
                                                          |Attack: {right_leg_attack}
                                                          |Defense: {right_leg_defense}
                                                          |Energy consumption: {right_leg_energy_consump}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''


robot_r2 = r"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=	
       0: {head_name}
       Is available: {head_status}
       Attack: {head_attack}                              
       Defense: {head_defense}
       Energy consumption: {head_energy_consump}
            ^
            |                  |1: {weapon_name}
            |                  |Is available: {weapon_status}
      ___       ___            |Attack: {weapon_attack}
     [___] /~\ [___]           |Defense: {weapon_defense}
     |ooo|.\_/.|ooo|           |Energy consumption: {left_arm_energy_consump}
     |888||   ||888|
  / /|888||   ||888|\ \
 /_./|###||___||###| \._\ ---> |2: {left_arm_name}
 /~\  ~~~ /[_]\ ~~~   /~\      |Is available: {left_arm_status}
(O_O) /~~[_____]~~\  (O_O)     |Attack: {left_arm_attack} 
     (  |       |  )            |Defense: {left_arm_defense}
    [~` ]       [ '~]           |Energy consumption: {left_arm_energy_consump}
    |~~|         |~~|           |
    |  |         |  |           |3: {right_arm_name}
   _<\/>_       _<\/>_          |Is available: {right_arm_status}
  /_====_\     /_====_\         |Attack: {right_arm_attack}                                
                                |Defense: {right_arm_defense}          
             ^                   |Energy consumption: {right_arm_energy_consump}
             |
             |    
|4: {left_leg_name} 
|Is available: {left_leg_status}
|Attack: {left_leg_attack}
|Defense: {left_leg_defense}
|Energy consumption: {left_leg_energy_consump}
|
|5: {right_leg_name}
|Is available: {right_leg_status}
|Attack: {right_leg_attack}
|Defense: {right_leg_defense}
|Energy consumption: {right_leg_energy_consump}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 """

robot_snakepiton = r"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=                            
                            0: Cabelça                               
                            Is available: {head_status}              
                            Attack: {head_attack}                              
                            Defense: {head_defense}                  
                            Energy consumption: {head_energy_consump}
                                           ^
                                           |
                                           |

 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠶⠟⠛⠛⠻⠶⠶⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⣡⣴⣾⣿⣿⣿⣶⣶⣦⣤⣉⣉⠛⠛⠷⢶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢉⣤⣾⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠛⠿⢷⣶⣤⣄⣉⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⢁⣴⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡟⠿⢶⣤⣄⠉⠻⣶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⢁⣴⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⣀⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠙⠓⠦⢄⣈⣻⣷⣄⠈⠻⣷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⢁⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⣠⣾⣿⣛⠛⠛⠻⣿⣇⠀⠀⠀⠀⣤⣄⣀⠀⠈⠉⠛⠻⠃⠀⠈⠻⣦⡀⠀ ---------> |1: Veneno Acido
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢁⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⢠⣾⡿⠋⠉⠛⠻⠶⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⣸⡇⠀            |Is available: {weapon_status}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⣰⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⢀⣴⡿⠿⠿⢷⣶⣤⣀⣀⠀⢹⣿⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⣠⡾⠟⠁⠀           |Attack: {weapon_attack}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⣼⣿⣿⣿⠟⠁⠀⠀⠀⠀⢀⣴⣿⣿⣀⡀⠀⠀⠀⠉⠙⠛⠻⢿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣇⣴⡟⠁⠀⠀⠀           |Defense: {weapon_defense}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⣸⣿⣿⣿⠋⠀⠀⠀⠀⠀⢠⣾⡟⠉⠉⠛⠛⠿⢷⣶⣤⣄⣀⠀⠀⢸⣿⡄⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀           |Energy consumption: {left_arm_energy_consump}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⢠⣿⣯⣀⣀⡀⠀⠀⠀⠀⠀⠈⠉⠙⠛⢿⣿⡿⢁⣀⠀⠀⠹⣿⣿⠟⠋⣹⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⢹⣿⣿⣇⠀⠀⠀⠀⠀⣿⡟⠉⠛⠛⠻⠿⠷⣶⣦⣤⣄⣀⣀⢀⣾⡟⣰⠟⠉⠳⣆⠀⠀⠀⣀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⢻⣿⣿⡄⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⣿⡿⢰⡏⠀⠀⠀⠈⠛⠶⠾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀------------> |2: Boca
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⢻⣿⣿⡀⠀⠀⠀⢹⣿⣦⣤⣤⣤⣤⣀⣀⣀⣀⣀⡀⢀⣿⡇⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀             |Is available: {left_arm_status}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣄⠀⢻⣿⣷⡀⠀⠀⠀⢿⣿⠉⠉⠉⠉⠙⠛⠛⠛⠛⠛⠻⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              |Attack: {left_arm_attack}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⢻⣿⣷⡀⠀⠀⠈⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                |Defense: {left_arm_defense}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⢻⣿⣿⡄⠀⠀⠘⣿⣦⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              |Energy consumption: {left_arm_energy_consump}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⠀⢻⣿⣿⡄⠀⠀⠘⣿⣏⠉⠉⠉⠉⠉⠀⠀⠀⢻⣿⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠻⣿⣿⡄⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠹⣿⣿⡄⠀⠀⠹⣿⣄⣤⣤⣤⣤⣤⣶⣾⣿⣧⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀------------>|3: Escama
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠹⣿⣿⡄⠀⠀⢹⣿⡉⠉⠁⠀⠀⠀⠀⢸⣿⡌⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              |Is available: {right_arm_status}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠹⣿⣿⡄⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⣿⣇⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              |Attack: {right_arm_attack} 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠹⣿⣿⡄⠀⠀⢿⣷⣤⣤⣴⣶⠶⠿⠿⣿⡌⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀             |Defense: {right_arm_defense}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡄⠹⣿⣿⡆⠀⠈⢿⣯⠀⠀⠀⠀⠀⠀⢿⣧⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              |Energy consumption: {right_arm_energy_consump}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠹⣿⣿⣄⠀⠘⣿⣧⠀⠀⢀⣀⣀⣼⣿⡄⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠹⣿⣿⡄⠀⠘⣿⣿⠟⠛⠋⠉⠉⢻⣷⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀------------>|4: Corpo
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠹⣿⣿⡄⠀⠘⣿⣆⠀⠀⠀⠀⣸⣿⡇⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              |Is available: {left_leg_status}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠹⣿⣿⡄⠀⠸⣿⣶⡶⠿⠛⠋⢻⣿⡘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀             |Attack: {left_leg_attack}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⢹⣿⣿⡀⠀⠹⣿⡄⠀⠀⠀⣀⣿⣧⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              |Defense: {left_leg_defense}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⢻⣿⣷⡀⠀⢹⣿⣶⠶⠟⠛⠻⣿⡄⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              ||Energy consumption: {left_leg_energy_consump}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⢻⣿⣧⠀⠀⢻⣿⠀⠀⠀⣀⣿⣧⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠒⠛⠛⠛⠒⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠈⢿⣿⣇⠀⠈⢿⣷⡶⠟⠛⠻⣿⡄⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠁⢀⣀⠀⢶⣶⣶⣤⡈⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠘⣿⣿⡆⠀⠘⣿⡆⠀⠀⣀⣿⣧⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⢀⣠⣾⡿⢿⣷⡄⠻⣿⣿⣿⣷⣄⡉⠳⣄⠀⠀⠀⠀⠀⠀⠀⣿⡀⢻⣿⣿⡀⠀⢻⣿⡾⠟⠋⢹⣿⡈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠞⠁⢀⣴⣿⠟⠉⠀⠀⠙⣿⣦⡈⠻⣿⣿⣿⣿⣦⡈⠻⣦⡀⠀⠀⠀⠀⢹⡇⠸⣿⣿⣇⠀⠘⣿⣆⣀⣤⣼⣿⡇⠻⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⠁⢀⣴⡿⠋⠁⠀⠀⠀⢀⣴⠟⠻⣿⣦⡈⠻⣿⣿⣿⣿⣷⣄⠙⢦⡀⠀⠀⢸⣷⠀⣿⣿⣿⠀⠀⣿⣿⠋⠉⠀⣿⡇⢠⣄⡉⠛⢶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢰⠋⠀⠀⠿⣿⣦⣄⡀⠀⢀⣴⡿⠁⠀⠀⢈⣿⢿⣶⣄⡙⠻⢿⣿⣿⣷⣦⡙⢷⣤⣸⣿⠀⣿⣿⣿⡇⠀⣿⣿⣤⣶⢾⣿⡇⢸⣿⣿⣷⣤⡈⠻⢦⡀⠀⠀    ---------> |5: Calda
⠀⠀⠀⠘⣧⠀⠀⠀⠈⠙⠻⢿⣷⣿⣏⡀⠀⠀⣠⡿⠃⠀⠉⢻⣿⣷⣦⣬⣙⣛⠻⠿⠶⠈⠻⠏⢠⣿⣿⣿⡇⠀⣿⡟⠉⠀⣸⣿⠃⢸⣿⣿⣿⡿⠟⢀⡀⠹⣦⠀               |Is available: {right_leg_status}
⠀⠀⣀⡴⠋⠀⣠⣤⣄⠀⠀⠀⠈⠉⠛⠿⣷⣶⣿⣀⡀⠀⢠⡿⠁⠀⠉⣹⡿⠛⠿⠿⣿⣿⠂⠀⣼⣿⣿⣿⠁⢠⣿⣷⡾⢿⣿⠏⠀⠉⠉⠉⢁⣀⣴⣿⣿⣆⠘⣧               |Attack: {right_leg_attack}
⣠⠞⠋⠀⠴⣾⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠈⠙⠛⠿⢿⣿⣷⣤⣤⣤⣿⣥⣤⣴⣿⠟⠁⢀⣼⣿⣿⣿⠏⢀⣾⡟⢁⣴⣿⠏⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿              |Defense: {right_leg_defense}
⠻⠦⣤⣀⡀⠀⠈⠉⠛⠻⠿⢿⣿⣷⣶⣤⣀⠘⠻⠶⣦⣤⣀⣉⠉⠙⠛⠛⠛⠉⠉⠀⣀⣴⣿⣿⣿⡿⠋⣠⣾⣿⣷⡿⠟⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⣰⠏              |Energy consumption: {right_leg_energy_consump}
⠀⠀⠀⠈⠉⠛⠓⠶⠦⣤⣄⣀⣀⡈⠉⠉⠛⠛⠷⠦⠀⠈⠉⠛⠛⠿⠿⠷⣾⣿⣿⣿⡿⠿⠿⠛⠁⠀⠀⠙⠛⠋⠁⠀⠀⠺⠿⠿⠿⠿⠟⠛⠛⣉⣁⣤⠶⠛⠁⠀              
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠲⠶⠶⠶⠤⠤⢤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠤⠤⠶⠶⠶⠒⠛⠛⠛⠛⠛⠛⠓⠚⠚⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 """

robots = {
    'origen': robot_origen,
    'ultron': robot_ultron,
    'r2': robot_r2,
    'snakepiton': robot_snakepiton,
}


colors = {
    "preto": '\x1b[90m',
    "azul": '\x1b[94m',
    "ciano": '\x1b[96m',
    "verde": '\x1b[92m',
    "magenta": '\x1b[95m',
    "vermelho": '\x1b[91m',
    "branco": '\x1b[97m',
    "amarelo": '\x1b[93m',
}


def get_part_status(self):
    part_status = {}
    for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
    return part_status


def build_robot():
    print("======"*10)
    robot_name = input("Nome do robô:")
    print("======"*10)
    selected_robot = choose_robot()
    color_code = choose_color()
    robot = Robot(robot_name, color_code, selected_robot)
    robot.print_status()
    return robot

def choose_robot():
    print("Robôs disponíveis:")
    for name in robots:
        print("- " + name.capitalize())
    while True:
        print("======"*10)
        robot_chosen = input("Escolha um Robô:").lower()
        print("======"*10)
        if robot_chosen in robots:
            selected_robot = robots[robot_chosen]
            break
        else:
            print("Robô invalido, escolha navamente.")
    return selected_robot

def choose_color():
    available_colors = colors
    print("Cores disponíveis:")
    for key, value in available_colors.items():
        print(value, key.capitalize())
    print(colors["preto"])
    while True:
        print("======"*10)
        chosen_color = input("Escolha uma cor:").lower()
        print("======"*10)
        if chosen_color in available_colors:
            color_code = available_colors[chosen_color]
            break
        else:
            print("""Cor invalida, escolha novamente.""")
    return color_code
def play():
    playing = True
    print('=-=-='*18)
    print("--------------Bem-vindo(a) ao jogo! Uma intensa batalha espera por você!------------------")
    print('=-=-='*18)
    print(" ")
    print('====='*12)
    print("-------Jogador 1, escolha com quem deseja batalhar----------")
    robot_one = build_robot()
    print('====='*12)
    print("-------Jogador 2, escolha com quem deseja batalhar----------")
    robot_two = build_robot()

    #current_robot = robot_one
    #enemy_robot = robot_two
    rount = 0

    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two      
        else:
            current_robot = robot_two
            enemy_robot = robot_one
        current_robot.print_status()
        print("Qual parte devo usar para atacar?")
        part_to_use = input("Escolha um número:")
        part_to_use = int(part_to_use)

        enemy_robot.print_status()
        print("Qual parte do inimigo devemos atacar?")
        part_to_attack = input("Escolha um número para atacar o inimigo:")
        part_to_attack = int(part_to_attack)

        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        rount += 1
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
             playing = False
             print('')
             print("Parabéns, você ganhou!")  




play()