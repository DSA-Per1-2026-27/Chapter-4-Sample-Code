"""
Simple example of a @dataclass
Create a class to store a Dungeons & Dragons character.
"""
from dataclasses import dataclass

@dataclass
class Character:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    armor_class: int
    hit_points: int
    max_hit_points: int
    ...

# The @dataclass decorator will *automatically* create an __init__ which
#   has all of these as keyword parameters

# If you have other stuff you wanted in __init__, the dataclass has a 
#   built-in method you can use called __post_init__ and that will run
#   automatically after the arguments get assigned to attributes.