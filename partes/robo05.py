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
