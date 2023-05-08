"""Template Method Pattern"""


class Character:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving")

    def attack(self):
        print(f"{self.name} is attacking")


class Warrior(Character):
    def attack(self):
        print(f"{self.name} is swinging a sword")


class Mage(Character):
    def attack(self):
        print(f"{self.name} is casting a spell")


class Archer(Character):
    def attack(self):
        print(f"{self.name} is shooting an arrow")


if __name__ == "__main__":
    warrior = Warrior("Conan")
    mage = Mage("Gandalf")
    archer = Archer("Legolas")

    warrior.move()
    warrior.attack()

    mage.move()
    mage.attack()

    archer.move()
    archer.attack()
