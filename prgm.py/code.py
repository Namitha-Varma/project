class GameCharacter:
    def __init__(self):
        self.__health = 100
        self.__energy = 50

    # Getter methods for child classes
    def get_health(self):
        return self.__health

    def get_energy(self):
        return self.__energy

    # Setter methods for child classes
    def set_health(self, value):
        if value < 0:
            self.__health = 0
        elif value > 100:
            self.__health = 100
        else:
            self.__health = value

    def set_energy(self, value):
        if value < 0:
            self.__energy = 0
        else:
            self.__energy = value

    def attack(self):
        if self.__energy < 10:
            print("Not enough energy!")
        else:
            self.__energy -= 10

    def take_damage(self, amount):
        self.__health -= amount

        if self.__health < 0:
            self.__health = 0

    def get_status(self):
        return f"Health: {self.__health}, Energy: {self.__energy}"


# Child Class 1
class Warrior(GameCharacter):

    def attack(self):
        super().attack()
        print("Warrior performs a heavy attack!")


# Child Class 2
class Mage(GameCharacter):

    def attack(self):
        if self.get_energy() >= 20:
            self.set_energy(self.get_energy() - 20)
            print("Mage casts a spell!")
        else:
            print("Not enough energy for spell!")

    def heal(self, amount):
        self.set_health(self.get_health() + amount)


# Test Code
w = Warrior()
m = Mage()

w.attack()
m.attack()

w.take_damage(30)
m.heal(20)

print(w.get_status())
print(m.get_status())