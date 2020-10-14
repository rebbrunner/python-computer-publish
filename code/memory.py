from RAM import RAM16K
from screen import Screen
from keyboard import Keyboard
from gates import dmux4way, mux4way16, or_gate

# Three sections, ram, screen, and keyboard.  When dmux'd into 4 bits, the first two reference ram.  In this case the first bit 
# sends the data to the first 8k sector while the second bit sends to the second half of the total 16k ram.  Keyboard does not
# write, it only reads.  The write operation should be called by the keyboard.

# Cheated a bit to speed it up - added an if section before the write operation to avoid the long write 
# operation if not necessary

class Memory:
    def __init__(self):
        pass
    
    def write(self, i, load, address):
        pass
