from inspect import getmembers, isabstract, isclass
import sys
from null_class import NoClass
from shipping_order import ShippingOrder


def get_commands():
    commands = (ShippingOrder,)
    return dict([cls.name, cls] for cls in commands)


def parse_commands(commands, args):
    command = commands.setdefault(args[0], NoClass)
    return command(args)


sys.argv.append("ShippingOrder")
sys.argv.append(2)

commands = get_commands()
command = parse_commands(commands, sys.argv[1:])
command.execute()