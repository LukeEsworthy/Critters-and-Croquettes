import attractions

print("Varmint Village is where you'll find snuggly animals to pet, like:")
for animal in attractions.varmint_village.animals:
    print(f"{animal.name} the {animal.species}")

print("Slither Inn is where you'll find slippery slimey monsters, like:")
for animal in attractions.slither_inn.animals:
    print(f"{animal.name} the {animal.species}")

print("Critter Cove is where you'll find a cove full of critters, like:")
for animal in attractions.critter_cove.animals:
    print(f"{animal.name} the {animal.species}")
