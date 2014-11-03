from QuackBehavior import QuackBehavior


class Quack(QuackBehavior):
    def __init__(self):
        super(Quack, self).__init__()

    def quack(self):
        print "Quack"
