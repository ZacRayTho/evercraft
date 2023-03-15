# You can write tests here or create new files in this directory with the name test_[something].py
from character import Character

# Tests
# Create a Character
def test_create_character():
    c = Character(name='Buddy', alignment='Good', armor="10")
    assert isinstance(c, Character)

# Character has a name
def test_character_name():
    c = Character(name='Buddy', alignment='Good', armor=10)
    assert hasattr(c, "name")

# Character can set name
def test_character_set_name():
    c = Character(name='Buddy', alignment='Good', armor=10)
    assert c.name == 'Buddy'

#### Feature: Create a Character
# > As a character I want to have a name so that I can be distinguished 
# from other characters - multiple characters
# - can get and set Name

def test_create_character_with_name_setter():
    character_name = "Cletus"
    c = Character(name='Buddy', alignment='Good', armor=10)
    c.name = character_name
    assert c.name == character_name

def test_create_character_with_default_name():
    character_name = "Cletus"
    c = Character(name=character_name, alignment="good", armor=10)
    assert c.name == character_name

def test_create_multiple_characters_with_diff_names():
    c1 = Character(name="Cletus", alignment="good", armor=10)
    c2 = Character(name="", alignment="good", armor=10)
    c2.name = "Fred"
    assert c1.name != c2.name

# Character can have alignment
def test_character_has_alignment():
    c = Character(name="bob", alignment="")
    assert hasattr(c, "alignment")

# Character can be Neutral
def test_character_alignment_neutral():
    c = Character(name="bob", alignment="neutral")
    assert c.alignment == "neutral"

# Character can be Good
def test_character_alignment_good():
    c = Character(name="bob", alignment="good")
    assert c.alignment == "good"

# Character can be Evil
def test_character_alignment_evil():
    c = Character(name="bob", alignment="evil", armor=10)
    assert c.alignment == "evil"
# Class for alignment?
#  
# Character has armor attribute
def test_character_has_armor():
    c = Character(name="bob", alignment="evil", armor=10)
    assert hasattr(c, "armor")

# Character has hit points (hp) attribute
def test_character_has_hp():
    c = Character(name="bob", alignment="evil", armor=10, hp=10)
    assert hasattr(c, "hp")

# Character armor defaults to 10
def test_character_armour_default():
    c = Character(name="bob", alignment="evil", armor=10, hp=10)
    assert c.armor == 10

# Character hp defaults to 5
def test_character_hp_default():
    c = Character(name="bob", alignment="evil", armor=10, hp=5)
    assert c.hp == 5

# Character needs to be able to attack another Character
def test_character_fight():
    c = Character(name="bob", alignment="evil", armor=10, hp=10)
    assert callable(c.fight)

# Character rolls a 20, attack succeeds
def test_character_roll_20():
    c = Character(name="bob", alignment="evil", armor=10, hp=10)
    z = Character(name="rob", alignment="evil", armor=10, hp=10)
    assert c.fight(20, z) == "NAT 20"

# Character rolls a 11, beats opp armor, attack succeeds
def test_character_roll_11():
    c = Character(name="bob", alignment="evil", armor=10, hp=10)
    z = Character(name="rob", alignment="evil", armor=10, hp=10)
    assert c.fight(11, z) == "success"

# Character rolls a 1, opp armor to much, attack fails
def test_character_roll_1():
    c = Character(name="bob", alignment="evil", armor=10, hp=10)
    z = Character(name="rob", alignment="evil", armor=10, hp=10)
    assert c.fight(1, z) == "fail"

# On successful attack, combatant loses hit points
def test_character_damage():
    c = Character(name="bob", alignment="evil", armor=10, hp=10)
    z = Character(name="rob", alignment="evil", armor=10, hp=10)
    c.fight(19, z)
    assert z.hp < 10

# On roll = 20, critical hit dealt, attack x2
def test_character_damage_on_20():
    c = Character(name="bob", alignment="evil", armor=10, hp=10)
    z = Character(name="rob", alignment="evil", armor=10, hp=10)
    c.fight(20, z)
    assert z.hp == 8

# Check hitpoints after successful attack, if <= 0, dead
def test_character_death():
    c = Character(name="bob", alignment="evil", armor=10, hp=10)
    z = Character(name="rob", alignment="evil", armor=10, hp=1, alive=True)
    c.fight(11, z)
    assert z.alive == False

# Character has an attribute of alive: true
def test_character_alive():
    c = Character(name="bob", alignment="evil", armor=10, hp=10, alive=True)
    assert hasattr(c, "alive")

# Character has Abilities that are Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma
def test_character_abilities():
    c = Character(name="bob", alignment="evil", armor=10, hp=10, alive=True, abilities={"strength": 10, "dexterity": 10, "constitution": 10, "wisdom": 10, "intelligence": 10, "charisma": 10})
    assert hasattr(c, "abilities")

# Abilities range from 1 to 20 and default to 10
def test_character_abilities_default():
    c = Character(name="bob", alignment="evil", armor=10, hp=10, alive=True, abilities={"strength": 10, "dexterity": 10, "constitution": 10, "wisdom": 10, "intelligence": 10, "charisma": 10})
    for ability in c.abilities:
        assert c.abilities[ability] == 10

#abilities can't go over 20
def test_character_abilities_max():
    c = Character(name="bob", alignment="evil", armor=10, hp=10, alive=True, abilities={"strength": 20, "dexterity": 10, "constitution": 10, "wisdom": 10, "intelligence": 10, "charisma": 10})
    for ability in c.abilities:
        assert not c.abilities[ability] > 20

# Abilities have modifiers according to the following table
# Score	Modifier	Score	Modifier	Score	Modifier	Score	Modifier
# 1	-5	6	-2	11	0	16	+3
# 2	-4	7	-2	12	+1	17	+3
# 3	-4	8	-1	13	+1	18	+4
# 4	-3	9	-1	14	+2	19	+4
# 5	-3	10	0	15	+2	20	+5
# Feature: Character Ability Modifiers Modify Attributes
# As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice

# add Strength modifier to:
# attack roll and damage dealt
# double Strength modifier on critical hits
# minimum damage is always 1 (even on a critical hit)
# add Dexterity modifier to armor class
# add Constitution modifier to hit points (always at least 1 hit point)
# Feature: A Character can gain experience when attacking
# As a character I want to accumulate experience points (xp) when I attack my enemies so that I can earn bragging rights at the tavern

# When a successful attack occurs, the character gains 10 experience points
# Feature: A Character Can Level
# As a character I want my experience points to increase my level and combat capabilities so that I can bring vengeance to my foes

# Level defaults to 1
# After 1000 experience points, the character gains a level
# 0 xp -> 1st Level
# 1000 xp -> 2nd Level
# 2000 xp -> 3rd Level
# etc.
# For each level:
# hit points increase by 5 plus Con modifier
# 1 is added to attack roll for every even level achieved
# You can write tests here or create new files in this directory with the name test_[something].py