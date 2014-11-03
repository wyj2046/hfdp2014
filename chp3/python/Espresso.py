from Beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        super(Espresso, self).__init__()

    def getDescription(self):
        return "Espresso"

    def cost(self):
        return 1.99
