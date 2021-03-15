from abs_commands import AbsCommand


class NoClass(AbsCommand):
    def __init__(self, args):
        self._command = args[0]

    def execute(self):
        print("Unknown command for {}".format(self._command))
