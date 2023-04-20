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
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
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
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["White"])

    def greet(self):
        print("Hello, my name is", self.name)

    def print_energy(self):
        print("We have", self.energy, " percent energy left")
