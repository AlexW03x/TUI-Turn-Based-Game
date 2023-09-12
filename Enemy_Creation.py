class Enemy():
    def __init__(self, name, hp, mp, power, speed, abilities):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_hp = hp
        self.max_mp = mp
        self.power = power
        self.speed = speed
        self.abilities = abilities

    def name(self):
        return self.name

    def hp(self):
        return self.hp

    def mp(self):
        return self.mp

    def max_hp(self):
        return self.max_hp

    def max_mp(self):
        return self.max_mp

    def power(self):
        return self.power

    def speed(self):
        return self.speed

    def abil(self):
        return self.abilities

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
        else:
            return False

