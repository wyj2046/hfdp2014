from FlyBehavior import FlyBehavior


class FlyWithWings(FlyBehavior):
    def __init__(self):
        super(FlyWithWings, self).__init__()

    def fly(self):
        print "I'm flying"
