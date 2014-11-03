class Beverage(object):
    def __init__(self):
        super(Beverage, self).__init__()
        self.description = "Unkown description"

    def getDescription(self):
        return self.description

    def cost(self):
        pass
