class Character():
    str = 10
    dex = 10
    con = 10
    wis = 10
    int = 10
    cha = 10

    modifiers = [-5,-4,-4,-3,-3,-2,-2,-1,-1,0,0,1,1,2,2,3,3,4,4,5]

    name = "Default Dan"
    alignment = 'Neutral'
    alive = True
    hp = 5

    # the '@property' decorator allows me to define a class method that can be accessed like a class attribute
    @property 
    def armor(self):
        return 10 + self.modifiers[self.dex - 1]

    def __init__(self, **attr):
        self.__dict__.update(attr)

    def attack(self, roll, enemy):
        if roll == 20:
            damage = ((1 + (self.modifiers[self.str - 1] * 2)) * 2)
            enemy.hp -= damage if damage > 0 else 1
            enemy.death_check()
            return True
        elif roll + self.modifiers[self.str - 1] >= enemy.armor:
            damage = 1 + self.modifiers[self.str - 1]
            enemy.hp -= damage if damage > 0 else 1
            enemy.death_check()
            return True

    def death_check(self):
        if self.hp <= 0:
            self.alive = False

c = Character(dex=12)

print(c.armor)