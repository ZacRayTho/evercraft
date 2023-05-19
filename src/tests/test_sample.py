# You can write tests here or create new files in this directory with the name test_[something].py
from character import Character

# Tests
# Create a Character
def test_create_character():
    c = Character()
    assert isinstance(c, Character)

# Character has a name
def test_character_name():
    c = Character()
    assert hasattr(c, "name")

# Character can get name
def test_character_get_name():
    c = Character()
    assert c.name == 'Default Dan'

# Character can set name after creation
def test_character_set_name():
    c = Character()
    c.name = 'Buddy'
    assert c.name == 'Buddy'

# Character can set name during creation
def test_character_set_name_as_created():
    c = Character(name='Buddy')
    assert c.name == 'Buddy'

# Character has alignment
def test_character_alignment():
    c = Character()
    assert hasattr(c, 'alignment')

# Character can set alignment
def test_character_alignment_set():
    c = Character(alignment='Good')
    assert c.alignment == 'Good'    

# Character has armor class
def test_character_armor():
    c = Character()
    assert hasattr(c, "armor")

# Character armor defaults to 10
def test_character_armor_default():
    c = Character()
    assert c.armor == 10

# Character has health points (hp)
def test_character_hp():
    c = Character()
    assert hasattr(c, "hp")

# Character hp defaults to 5
def test_character_hp_default():
    c = Character()
    assert c.hp == 5

# Character can attack
def test_character_attack():
    c = Character()
    assert callable(getattr(c, "attack"))

# Character attack roll meets enemy (armor class) AC is a hit
def test_character_attack_roll_meet_ac():
    c = Character()
    z = Character()
    assert c.attack(10, z)

# Character attack roll exceeds enemy AC is a hit
def test_character_attack_roll_exceed_ac():
    c = Character()
    z = Character() 
    assert c.attack(19, z)

# Character attack roll under enemy AC is a miss
def test_character_attack_roll_under_ac():
    c = Character()
    z = Character()
    assert not c.attack(3, z)

# Character takes 1 damage on successful attack roll
def test_character_damage():
    c = Character()
    z = Character()
    c.attack(12, z)
    assert z.hp == 4

# Character takes double damage on attack roll of 20
def test_character_damage_nat20():
    c = Character()
    z = Character()
    c.attack(20, z)
    assert z.hp == 3

# Character is dead when hp are 0 or less
def test_character_death():
    c = Character()
    z = Character()
    c.attack(20, z)
    c.attack(20, z)
    c.attack(20, z)
    assert z.alive == False

# Character has Strength ability
def test_character_strength():
    c = Character()
    assert hasattr(c, 'str')

# Character has Dexterity ability
def test_character_dexterity():
    c = Character()
    assert hasattr(c, 'dex')

# Character has Constitution ability
def test_character_constitution():
    c = Character()
    assert hasattr(c, 'con')

# Character has Wisdom ability
def test_character_wisdom():
    c = Character()
    assert hasattr(c, 'wis')

# Character has Intelligence ability
def test_character_intelligence():
    c = Character()
    assert hasattr(c, 'int')

# Character has Charisma ability
def test_character_charisma():
    c = Character()
    assert hasattr(c, 'cha')

# Character Abilities range can't go below 1-------------------------------------------------------
# Character Abilities range can't go above 20

# Character has Strength ability
def test_character_strength_default():
    c = Character()
    assert c.str == 10

# Character has Dexterity ability
def test_character_dexterity_default():
    c = Character()
    assert c.dex == 10

# Character has Constitution ability
def test_character_constitution_default():
    c = Character()
    assert c.con == 10

# Character has Wisdom ability
def test_character_wisdom_default():
    c = Character()
    assert c.wis == 10

# Character has Intelligence ability
def test_character_intelligence_default():
    c = Character()
    assert c.int == 10

# Character has Charisma ability
def test_character_charisma_default():
    c = Character()
    assert c.cha == 10

# Character's strength modifier is added to attack roll
def test_character_str_mod_attack():
    c = Character()
    z = Character()
    c.str = 20
    assert c.attack(5, z)

# Character's strength modifier is added to attack roll
def test_character_str_mod_damage():
    c = Character()
    z = Character()
    c.str = 12
    c.attack(10, z)
    assert z.hp == 3

# Character's strength modifier is doubled on critical hit
def test_character_str_mod_crit():
    c = Character()
    z = Character()
    c. str = 12
    c.attack(20,z)
    assert z.hp == -1

# Character's minimum attack always 1
def test_character_str_mod_min_attack():
    c = Character()
    z = Character()
    c. str = 1
    c.attack(20,z)
    assert z.hp == 4

# Character's Dexterity modifier is added to armor
def test_character_dex_mod_armor():
    c = Character(dex=12)
    assert c.armor == 11



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