from Beverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        super(DarkRoast, self).__init__()

    def getDescription(self):
        return "Dark Roast"

    def cost(self):
        return 0.99
