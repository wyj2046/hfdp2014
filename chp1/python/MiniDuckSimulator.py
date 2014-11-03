from MallardDuck import MallardDuck
from ModelDuck import ModelDuck
from FlyRocketPowered import FlyRocketPowered


def main():
    mallard = MallardDuck()
    mallard.performFly()
    mallard.performQuack()
    print "**********"
    model = ModelDuck()
    model.performFly()
    model.performQuack()
    model.setFlyBehavior(FlyRocketPowered())
    model.performFly()

if __name__ == '__main__':
    main()
