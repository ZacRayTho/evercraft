# You can write tests here or create new files in this directory with the name test_[something].py
from character import Character, Fighter, Rogue, Monk, Paladin

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
    assert hasattr(c, 'inte')

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
    assert c.inte == 10

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

# Character's Constitution modifier is added to hp
def test_character_con_mod_hp():
    c = Character(con=12)
    assert c.hp == 6

# Character's always has 1 hp regardless of constitution mod
def test_character_con_mod_min_hp():
    c = Character(con=1)
    assert c.hp == 1

# Character gains 10 xp after successful attack
def test_character_exp_gain():
    c = Character()
    z = Character()
    c.attack(12, z)
    assert c.exp == 10

# Character's level defaults to 1
def test_character_level():
    c = Character()
    assert c.level == 1

# Character's max_hp increase by 5 + con mod for each level
def test_character_hp_increase():
    c = Character(exp=1000)
    assert c.max_hp == 10

# Character gets +1 added to attack roll for every even level gained
def test_character_attack_roll_increase():
    c = Character(exp=1000)
    z = Character()
    assert c.attack(9, z)

# Character can become a fighter class
def test_character_fighter_class():
    c = Fighter()
    assert isinstance(c, Fighter)

# Fighter class attack rolls increase by 1 for every level instead of every other level
def test_character_fighter_attack():
    c = Fighter(exp=2000)
    z = Character()
    assert c.attack(8, z)

# Fighter class has 10 hp per level instead of 5
def test_character_fighter_hp():
    c = Fighter()
    assert c.hp == 10

# Character can become Rogue class
def test_character_rogue_class():
    c = Rogue()
    assert isinstance(c, Rogue)

# Rogue class does triple damage on crits
def test_character_rogue_crit_damage():
    c = Rogue()
    z = Character()
    c.attack(20, z)
    assert z.hp == 2

# Rogue class ignores opponent dex mod to armor when attacking
def test_character_rogue_ignore_dex():
    c = Rogue()
    z = Character(dex=12)
    assert c.attack(10, z)

# Rogue class can't be Good Alignment
def test_character_rogue_alignment():
    c = Rogue(alignment="Good")
    assert c.alignment != "Good"

# Character can become Monk class
def test_character_monk_class():
    c = Monk()
    assert isinstance(c, Monk)

# Monk class has 10 hp per level instead of 5
def test_character_monk_hp():
    c = Monk()
    assert c.hp == 6

# Monk class does 3 damage on successful attack
def test_character_monk_attack():
    c = Monk()
    z = Character()
    c.attack(10, z)
    assert z.hp == 2

# Monk class added wisdom modifier to armor if positive
def test_character_monk_wisdom_armor():
    c = Monk(wis=12)
    assert c.armor == 11

# Character can become Paladin Class
def test_character_paladin_class():
    c = Paladin()
    assert isinstance(c, Paladin)

# Paladin has 8 hp level instead of 5
def test_character_paladin_hp():
    c = Paladin()
    assert c.hp == 8

# Paladin gets +2 to attack roll and damage when attacking Evil characters
def test_character_paladin_attack_evil():
    c = Paladin()
    z = Character(alignment="Evil")
    c.attack(8, z)
    assert z.hp == 2

# Paladin crits times 3 when attacking Evil character
def test_character_paladin_crit_evil():
    c = Paladin()
    z = Character(alignment="Evil")
    c.attack(20, z)
    assert z.hp == -4

# Paladin attack rolls increased by 1 for every level
def test_character_paladin_attack_roll():
    c = Paladin()
    z = Character()
    assert  c.attack(9, z)

# Paladin can only be Good alignment
def test_character_paladin_good_only():
    c = Paladin(alignment="Evil")
    assert c.alignment == "Good"
# You can write tests here or create new files in this directory with the name test_[something].py