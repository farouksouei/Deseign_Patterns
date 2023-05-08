class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        return self.component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self.component.operation()})"


if __name__ == "__main__":
    component = ConcreteComponent()
    decorator_a = ConcreteDecoratorA(component)
    decorator_b = ConcreteDecoratorB(decorator_a)
    print(decorator_b.operation())  # Output: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
