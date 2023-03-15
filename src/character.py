class Character():
    def __init__(self, **attr):
        self.__dict__.update(attr)

    def fight(self, roll, victim):
        if roll == 20:
            victim.hp -= 2
            victim.check_life()
            return "NAT 20"
        elif roll > victim.armor:
            victim.hp -= 1
            victim.check_life()
            return "success"
        else:
            return "fail"

    def check_life(self):
        if self.hp <= 0:
            self.alive = False