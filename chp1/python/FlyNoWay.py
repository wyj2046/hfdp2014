from FlyBehavior import FlyBehavior


class FlyNoWay(FlyBehavior):
    def __init__(self):
        super(FlyNoWay, self).__init__()

    def fly(self):
        print "I can't fly"
