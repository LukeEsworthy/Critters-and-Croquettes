from datetime import date


class BillyGoat:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Otter:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class BoaConstrictor:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Warthog:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Piranha:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Hellbender:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Camel:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Pike:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Copperhead:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Gorilla:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Lionfish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class KingCobra:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Cheetah:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class MorayEel:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class BlackMamba:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."


bilbo = BillyGoat("Bilbo", "Billy Goat", "Morning", "feed pellets")
otto = Otter("Otto", "Asian small-clawed otter", "crayfish")
bo = BoaConstrictor("Bo", "Argentine Boa", "fluffy little rabbits")
pumbaa = Warthog("Pumbaa", "Gluttonous warthog", "Midday", "grass")
snuggles = Piranha("Snuggles", "Red-bellied piranha", "kid fingers")
pinhead = Hellbender("Pinhead", "Ozark hellbender", "crayfish")
mike = Camel("Mike", "One-humped dromedary camel", "Afternoon", "grass")
lance = Pike("Lance", "Northern pike", "fish")
steve = Copperhead("Steve", "Southern copperhead", "mice")
kong = Gorilla("Kong", "Silverback gorilla", "Morning", "bamboo shoots")
lonny = Lionfish("Lonny", "Spotfin lionfish", "shrimp")
jafar = KingCobra("Jafar", "Ophiophagus hannah king cobra", "lizards")
speedy = Cheetah("Speedy", "South African cheetah", "Midday", "gazelle")
vizzini = MorayEel("Vizzini", "Giant moray eel", "fish")
tanya = BlackMamba("Tanya", "Dendroaspis polylepis black mamba", "rodents")

print(bilbo.name)
print(otto.name)
print(bo.name)
print(pumbaa.name)
print(snuggles.name)
print(pinhead.name)
print(mike.name)
print(lance.name)
print(steve.name)
print(kong.name)
print(lonny.name)
print(jafar.name)
print(speedy.name)
print(vizzini.name)
print(tanya.name)


print(f"{speedy.name} the {speedy.species} is available to pet during the {speedy.shift} shift.")

print(lonny)


class PettingZoo:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)


class SnakePit:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)


class Wetlands:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)


varmint_village = PettingZoo(
    "Varmint Village", "Completely harmless and not-at-all dangerous animals to pet")
varmint_village.add_animal(bilbo)
varmint_village.add_animal(pumbaa)
varmint_village.add_animal(mike)
varmint_village.add_animal(kong)
varmint_village.add_animal(speedy)

slither_inn = SnakePit("Slither Inn", "A better pit than Brad Pitt")
slither_inn.add_animal(bo)
slither_inn.add_animal(pinhead)
slither_inn.add_animal(steve)
slither_inn.add_animal(jafar)
slither_inn.add_animal(tanya)

critter_cove = Wetlands("Critter Cove", "Like drylands, but wetter")
critter_cove.add_animal(otto)
critter_cove.add_animal(snuggles)
critter_cove.add_animal(lance)
critter_cove.add_animal(lonny)
critter_cove.add_animal(vizzini)

print("Varmint Village is where you'll find snuggly animals to pet, like:")
for animal in varmint_village.animals:
    print(f"{animal.name} the {animal.species}")

print("Slither Inn is where you'll find slippery slimey monsters, like:")
for animal in slither_inn.animals:
    print(f"{animal.name} the {animal.species}")

print("Critter Cove is where you'll find a cove full of critters, like:")
for animal in critter_cove.animals:
    print(f"{animal.name} the {animal.species}")
