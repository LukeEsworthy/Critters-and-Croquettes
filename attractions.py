import animals


class PettingZoo:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_animal_added(self):
        return f"{self.animals[-1]}"


class SnakePit:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_animal_added(self):
        return f"{self.animals[-1]}"


class Wetlands:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_animal_added(self):
        return f"{self.animals[-1]}"


varmint_village = PettingZoo(
    "Varmint Village", "Completely harmless and not-at-all dangerous animals to pet")
varmint_village.add_animal(animals.bilbo)
varmint_village.add_animal(animals.pumbaa)
varmint_village.add_animal(animals.mike)
varmint_village.add_animal(animals.kong)
varmint_village.add_animal(animals.speedy)

slither_inn = SnakePit("Slither Inn", "A better pit than Brad Pitt")
slither_inn.add_animal(animals.bo)
slither_inn.add_animal(animals.pinhead)
slither_inn.add_animal(animals.steve)
slither_inn.add_animal(animals.jafar)
slither_inn.add_animal(animals.tanya)

critter_cove = Wetlands("Critter Cove", "Like drylands, but wetter")
critter_cove.add_animal(animals.otto)
critter_cove.add_animal(animals.snuggles)
critter_cove.add_animal(animals.lance)
critter_cove.add_animal(animals.lonny)
critter_cove.add_animal(animals.vizzini)

print("testing dynamic duo", varmint_village.last_animal_added)
print("testing dynamic duo", critter_cove.last_animal_added)
print("testing dynamic duo", slither_inn.last_animal_added)
