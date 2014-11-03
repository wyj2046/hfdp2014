from Beverage import Beverage
from Espresso import Espresso
from DarkRoast import DarkRoast
from HouseBlend import HouseBlend
from Soy import Soy
from Whip import Whip
from Mocha import Mocha


def main():
    beverage = Espresso()
    print beverage.getDescription() + " $" + str(beverage.cost())

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print beverage2.getDescription() + " $" + str(beverage2.cost())

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print beverage3.getDescription() + " $" + str(beverage3.cost())

if __name__ == '__main__':
    main()
