import argparse

from hack_parser import Parser
from translator import Code
from symbol_table import SymbolTable

class Assembler:
    def __init__(self, filename):
        pass

    def first_pass(self):
        pass

    def is_variable(self, symbol):
        pass

    def second_pass(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename

    assembler = Assembler(filename)
    assembler.first_pass()
    assembler.second_pass()
