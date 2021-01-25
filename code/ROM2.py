from ast import literal_eval

# Not really ROM, as the file that's being read in can be changed.  But more flexible.
# Loads the program to be executed, written in csv style with 16 bit instructions written in T/F

class ROM32K:
    def __init__(self):
        with open('./programs/program.hack') as f:
            instructions = f.read().splitlines()
            instructions = [instruction for instruction in instructions if instruction.strip()]

        self.instructions = [[literal_eval(bit) for bit in instruction.split(' ')] for instruction in instructions]

    def read(self, address):
        binary = int(''.join(['0' if not bit else '1' for bit in address]), 2)
        try:
            return self.instructions[binary]
        except:
            return self.instructions[0]
