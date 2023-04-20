
def attack(self, enemy_robot, part_to_use, part_to_attack):
    enemy_robot.parts[part_to_attack].reduce_edefense(
        self.parts[part_to_use].attack_level)
    self.energy -= self.parts[part_to_use].energy_consumption
