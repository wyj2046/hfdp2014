from Duck import Duck
from FlyNoWay import FlyNoWay
from Quack import Quack


class ModelDuck(Duck):
    def __init__(self):
        # super(ModelDuck, self).__init__()
        self.setFlyBehavior(FlyNoWay())
        self.setQuackBehavior(Quack())

    def display(self):
        print "I'm a model duck"
