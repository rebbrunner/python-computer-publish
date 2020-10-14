from gates import mux16_gate, not_gate, or_gate, and_gate
from RAM import Register
from ALU import ALU_chip
from PC import ProgramCounter

# The CPU consists of three elements: memory, the ALU, and a program counter
# The memory is three registers, the address register, data register, and technically the instruction register in the pc
# The address register is used for finding locations in memory
# The data register is used for storing output from the ALU
# The instruction register is the number of the current step being processed
# The ALU is a function that performs different actions based on the current instruction
# The program counter helps step the alu through a set of instructions including various kinds of jumps

class CPU:
    def __init__(self):
        pass
    
    # ALU runs twice to simulate full clock cycle.  General idea - run ALU first, then perform load operations, just like in normal programming
    # (a = 1 + 1, 1 + 1 is performed before assignment operation).  The ALU is then ran again with updated values to produce good output to 
    # memory
    def run(self, inM, instruction, reset):
        pass
