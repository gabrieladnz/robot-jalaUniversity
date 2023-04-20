class Part():
    # características do robô
    def __init__(self, nome: str, nivelAtaque=0, nivelDefesa=0, energiaConsumida=0):
        self.nome = nome
        self.nivelAtaque = nivelAtaque
        self.nivelDefesa = nivelDefesa
        self.energiaConsumida = energiaConsumida

    # função que contém e retorna um dicionário com os dados do robô
    def get_status_dict(self):
        formatted_name = self.nome.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.nome.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.nivelAtaque,
            "{}_defense".format(formatted_name): self.nivelDefesa,
            "{}_energy_consump".format(formatted_name): self.energiaConsumida,
        }

    def reduce_edefense(self, nivelAtaque):
        self.nivelDefesa = self.nivelDefesa - nivelAtaque
        if self.nivelDefesa <= 0:
            self.nivelDefesa = 0

    def is_available(self):
        return self.nivelDefesa <= 0


class Robot:
    def __init__(self, name, color_code):
        self.nome = nome
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("Head", nivelAtaque=5, nivelDefesa=10, energiaConsumida=5),
            Part("Weapon", nivelAtaque=15,
                 nivelDefesa=0, energiaConsumida=10),
            Part("Left Arm", nivelAtaque=3,
                 nivelDefesa=20, energiaConsumida=10),
            Part("Right Arm", nivelAtaque=6,
                 nivelDefesa=20, energiaConsumida=10),
            Part("Left Leg", nivelAtaque=4,
                 nivelDefesa=20, energiaConsumida=15),
            Part("Right Leg", nivelAtaque=8,
                 nivelDefesa=20, energiaConsumida=15),
        ]

    def print_status(self):
        print(self.color_code)
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["White"])

    def greet(self):
        print("Hello, my name is", self.nome)

    def print_energy(self):
        print("We have", self.energy, " percent energy left")

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
        enemy_robot.parts[part_to_attack].reduce_edefense(
            self.parts[part_to_use].nivelAtaque)
        self.energy -= self.parts[part_to_use].energiaConsumida


robot_art = r"""
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

 """

colors = {
    "Black": '\x1b[90m',
    "Blue": '\x1b[94m',
    "Cyan": '\x1b[96m',
    "Green": '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Red": '\x1b[91m',
    "White": '\x1b[97m',
    "Yellow": '\x1b[93m',
}

def get_part_status(self):
    part_status = {}
    for part in self.parts:
        status_dict = part.get_status_dict()
        part_status.update(status_dict)
    return part_status


def build_robot():
    robot_name = input("Robot name: ")
    color_code = choose_color()
    robot = Robot(robot_name, color_code)
    robot.print_status()
    return robot


def choose_color():
    available_colors = colors
    print("Available colors:")
    for key, value in available_colors.items():
        print(value, key)
    print(colors["White"])
    chosen_color = input("Choose a color: ")
    color_code = available_colors[chosen_color]
    return color_code


def play():
    playing = True
    print("Welcome to the game!")
    print("Datas for player 1:")
    robot_one = build_robot()
    print("Datas for player 2:")
    robot_two = build_robot()

    current_robot = robot_one
    enemy_robot = robot_two
    rount = 0

    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one
        current_robot.print_status()
        print("What part should I use to attack?:")
        part_to_use = input("Choose a number part: ")
        part_to_use = int(part_to_use)

        enemy_robot.print_status()
        print("Which part of the enemy should we attack?")
        part_to_attack = input("Choose a enemy number part to attack: ")
        part_to_attack = int(part_to_attack)

        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        rount += 1
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            print("Congratulations, you won")


play()