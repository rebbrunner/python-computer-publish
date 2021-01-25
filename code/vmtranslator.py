import os
import argparse

from vmparser import Parser
from vmcodewriter import CodeWriter

# Parses through .vm file and translates operations into assembly
# Uses two components, CodeWriter and Parser
# CodeWriter is in charge of writing the actual translations to an output file
# Parser walks through each line of vm code and classifies lines into categories
# Categories are: ARITHMETIC/LOGICAL, PUSH, POP, FUNCTION, RETURN, IF, LABEL, GOTO, and CALL

class Translator:
    def __init__(self, filename):
        pass

    def translate(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename

    vm_translator = Translator(filename)
    vm_translator.translate()
