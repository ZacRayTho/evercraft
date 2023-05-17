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