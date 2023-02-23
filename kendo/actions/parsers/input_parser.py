from .action_parser import ActionParser


class InputParser:
    def __init__(self, pessoa):
        self._pessoa = pessoa

    def execute_command(self, input_string):
        split = str(input_string).split()
        return ActionParser(split[0], split[1], self._pessoa).find_command()
