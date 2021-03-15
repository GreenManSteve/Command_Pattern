from abs_order_command import AbsOrderCommand
from abs_commands import AbsCommand


class ShippingOrder(AbsCommand, AbsOrderCommand):
    name = "ShippingOrder"
    description = "Shipping Order command"

    def __init__(self, args):
        self._newQnty = args[1]

    def execute(self):
        print("The command is {} and the value is {}".format(self.name,self._newQnty))

