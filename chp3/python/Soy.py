from CondimentDecorator import CondimentDecorator


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        super(Soy, self).__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Soy"

    def cost(self):
        return self.beverage.cost() + 0.15
