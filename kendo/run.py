from actions.parsers.input_parser import InputParser
from actions.models.pessoa import Pessoa

command_string = str(input('digite aqui queridão: '))
output_string = InputParser(Pessoa()).execute_command(command_string)
print(output_string)
