from Beverage import Beverage


class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__()

    def getDescription(self):
        return "House Blend Coffee"

    def cost(self):
        return 0.89
