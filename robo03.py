
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
