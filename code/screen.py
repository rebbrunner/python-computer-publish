from RAM import RAM4K
from gates import mux16_gate, dmux_gate
import pygame
import numpy

# A memory chip to interface with a simulated screen.  Memory map can be read in by a screen to turn individual pixels on/off
# Changes: For virtual screen - started using pygame (which should also cover keyboard) and numpy
# Pixel values are stored in a numpy array for easy conversion into a 2d array
# Pixels are updated 16 at a time
# After updaing the memory map, the virtual screen is updated as well
# Screen size is 512x256, with each row having 32 16-bit words for a total of 8,192 words which in the book is equivalent to the 
# 8k RAM chip

class Screen:
    def __init__(self):
        # Memory map is now a numpy array for speed.  Initial value is 255 for a white screen
        self.mem_map = numpy.full(512*256, 255)

        # Setup pygame window
        self.screen = pygame.display.set_mode((512, 256))
    
    def write(self, i, load, address):
        # Translate T/F address into decimal number
        decimal_address = int(''.join(['0' if not bit else '1' for bit in address]), 2)
        
        # Screen updates pixels 16 at a time
        index = decimal_address*16

        # Screen is initially black, invert
        if load:
            pixels = [0 if bit == True else 255 for bit in i]
            self.mem_map[index:index+16] = pixels

        # pygame does a weird inversion thing requiring axes to be swapped before render
        mem_map2d = self.mem_map.reshape((256, 512))
        mem_map2d = numpy.swapaxes(mem_map2d, 0, 1)
        surf = pygame.surfarray.make_surface(mem_map2d)
        self.screen.blit(surf, (0, 0))
        pygame.display.update()

        return self.mem_map[index:index+16]


if __name__ == '__main__':
    address =  [False, False, False, False, False, False, False, False, False, False, False, False, False]
    i =  [True, True, True, True, True, True, False, False, False, False, True, True, True, True, True, True]
    screen = Screen()
    screen.write(i, True, address)

    # Loop allows pygame window to stay up
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # If a key is being pressed down get the keycode as a binary format
                print('{0:016b}'.format(event.key))
            if event.type == pygame.QUIT:
                pygame.quit()
