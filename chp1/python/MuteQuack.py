from QuackBehavior import QuackBehavior


class MuteQuack(QuackBehavior):
    def __init__(self):
        super(MuteQuack, self).__init__()

    def quack(self):
        print "<< Silence >>"
