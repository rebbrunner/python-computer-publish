from RAM import Register

# This chips should allow the computer to accept input from a keyboard simulation.  The 'keyboard' will call the write function, 
# which can then be read by the computer

class Keyboard:
    def __init__(self):
        self.keyboard = [False for i in range(16)]
    
    def write(self, i, load):
        return self.keyboard
