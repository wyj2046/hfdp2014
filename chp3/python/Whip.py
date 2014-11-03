from CondimentDecorator import CondimentDecorator


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        super(Whip, self).__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"

    def cost(self):
        return self.beverage.cost() + 0.10
