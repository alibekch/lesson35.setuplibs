class Grade:
    def __init__(self, name, persons):
        self.name = name
        self.persons = persons

    def print_persons(self):
        for a in self.persons:
            print(a.getFullName())