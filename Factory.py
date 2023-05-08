class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"


class AnimalFactory:
    def get_animal(self, animal_type, name):
        if animal_type == 'dog':
            return Dog(name)
        elif animal_type == 'cat':
            return Cat(name)
        else:
            return None


if __name__ == "__main__":
    animal_factory = AnimalFactory()
    dog = animal_factory.get_animal('dog', 'Rufus')
    print(dog.speak())  # Output: Woof!
