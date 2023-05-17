class Character():
    name = ""
    armor = 10
    hp = 5

    def __init__(self, **attr):
        self.__dict__.update(attr)

