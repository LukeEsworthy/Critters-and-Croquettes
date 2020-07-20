from datetime import date


class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.chip_num = chip_num
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}."

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, num):
        pass


class BillyGoat(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True


class Otter(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}, while being hummed the lullaby from \"Pan\'s Labyrinth\".')


class BoaConstrictor(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Warthog(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True


class Piranha(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class Hellbender(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Camel(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True


class Pike(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class Copperhead(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Gorilla(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True


class Lionfish(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class KingCobra(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}, while he listened to his favorite flute solo.')


class Cheetah(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True


class MorayEel(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}, while \"Princess Bride\" played on TV.')


class BlackMamba(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


bilbo = BillyGoat("Bilbo", "Billy Goat", "Morning", "feed pellets", 1111)
otto = Otter("Otto", "Asian small-clawed otter", "crayfish", 2222)
bo = BoaConstrictor("Bo", "Argentine Boa", "fluffy little rabbits", 3333)
pumbaa = Warthog("Pumbaa", "Gluttonous warthog", "Midday", "grass", 4444)
snuggles = Piranha("Snuggles", "Red-bellied piranha", "kid fingers", 5555)
pinhead = Hellbender("Pinhead", "Ozark hellbender", "crayfish", 6666)
mike = Camel("Mike", "One-humped dromedary camel", "Afternoon", "grass", 7777)
lance = Pike("Lance", "Northern pike", "fish", 8888)
steve = Copperhead("Steve", "Southern copperhead", "mice", 9999)
kong = Gorilla("Kong", "Silverback gorilla", "Morning", "bamboo shoots", 1212)
lonny = Lionfish("Lonny", "Spotfin lionfish", "shrimp", 2323)
jafar = KingCobra("Jafar", "Ophiophagus hannah king cobra", "lizards", 3434)
speedy = Cheetah("Speedy", "South African cheetah", "Midday", "gazelle", 4545)
vizzini = MorayEel("Vizzini", "Giant moray eel", "fish", 5656)
tanya = BlackMamba(
    "Tanya", "Dendroaspis polylepis black mamba", "rodents", 6767)

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
print(otto.feed())
print(jafar.feed())
print(vizzini.feed())
