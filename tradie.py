class Tradie:

    def __init__(self, name, company, skill):
        self.name = name
        self.company = company
        self.skill = skill

    def __str__(self):
        return f"Name: {self.name}, Company: {self.company}, Service: {self.skill}"