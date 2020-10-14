from gates import mux16_gate
from adders import inc16_chip
from RAM import Register

# In imperative languages such as the HDL used in nand2tetris, code can be circular; input can be output. 
# This does not work in a procedural settting.  Using classes like with memory, execution can be made procedural.
# Each call of the program counter is one full execution cycle

class ProgramCounter:
    def __init__(self):
        pass
    
    def run(self, i, load, inc, reset):
        pass
