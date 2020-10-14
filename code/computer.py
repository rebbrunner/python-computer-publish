from ROM2 import ROM32K
from CPU import CPU
from memory import Memory

import pygame

# The entire computer in three lines of code.  Takes one input, the reset button.  Technically the computer should just 
# continually call run forever, only resetting the pc.  However we can use python to stop the computer once it finishes 
# executing all instructions.  Run operation should be called for every line in ROM.

class Computer:
    def __init__(self):
        pass
    
    def run(self, reset):
        pass

# Testing code
if __name__ == '__main__':
    computer = Computer()

    # Input for certain test operations relies on data being preset in RAM
    #computer.ram.write([False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False], True, [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False])
    #computer.ram.write([False, False, True, True, False, False, False, False, False, False, True, True, True, False, False, True], True, [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True])

    # Instead of infinitely looping, get the end of file for the input program
    # When the program counter reaches past the point, break execution loop
    def get_end(pc):
        pc = '{0:015b}'.format(pc)
        return [False if bit == '0' else True for bit in pc]
    
    stop = len(computer.rom.instructions) + 1
    end = get_end(stop)

    # This loop executes each instruction via computer.run()
    # Keyboard input is set in this loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = '{0:016b}'.format(event.key)
                key = [False if bit == '0' else True for bit in key]
                computer.ram.keyboard.keyboard = key
            else:
                key = [False for i in range(16)]
                computer.ram.keyboard.keyboard = key
            if event.type == pygame.QUIT:
                pygame.quit()
        computer.run(False)
        if computer.pc == end:
            break

    # For operations that set RAM, this gets RAM[2] to check result
    dummy = [False for i in range(16)]
    address = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False]
    res = computer.ram.write(dummy, False, address)
    res = ['0' if char == False else '1' for char in res]
    res = ''.join(res)
    res = int(res, 2)
    print(res)
