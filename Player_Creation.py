class Player():
    def __init__(self, name, hp, mp, power, speed, class_type, level):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_hp = hp
        self.max_mp = mp
        self.power = power
        self.speed = speed
        self.class_type = class_type

        self.level = level

    def modify(self, var, modifier):
        if var == "name":
            self.name = modifier
        elif var == "hp":
            self.hp = modifier
        elif var == "mp":
            self.mp = modifier
        elif var == "max_hp":
            self.max_hp = modifier
        elif var == "max_mp":
            self.max_mp = modifier
        elif var == "power":
            self.power = modifier
        elif var == "speed":
            self.speed = modifier
        elif var == "abilities":
            self.abilities = modifier
        elif var == "level":
            self.level = modifier
        else:
            return False

    def name():
        return self.name

    def hp():
        return self.hp

    def mp():
        return self.mp

    def max_hp():
        return self.max_hp

    def max_mp():
        return self.max_mp

    def power():
        return self.power

    def speed():
        return self.speed

    def abil():
        return self.abilities

    def level():
        return self.level

    def classtype():
        return self.class_type
##tests##
#p = Player("Jimmy", 165, 70, 11, 8, "Hybrid", 1)
#p.modify("hp", 500)

