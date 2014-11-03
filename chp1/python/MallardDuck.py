from Duck import Duck
from FlyWithWings import FlyWithWings
from Quack import Quack


class MallardDuck(Duck):
    def __init__(self):
        # super(MallardDuck, self).__init__()
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(Quack())

    def display(self):
        print "I'm a real Mallard duck!"


if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.display()
    mallard.performFly()
    mallard.performQuack()
