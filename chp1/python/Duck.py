class Duck(object):
    def __init__(self):
        # super(Duck, self).__init__()
        pass

    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print "All ducks float, even decoys!"

    def setFlyBehavior(self, fb):
        self.flyBehavior = fb

    def setQuackBehavior(self, qb):
        self.quackBehavior = qb
