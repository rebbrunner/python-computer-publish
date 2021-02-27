from gates import dmux8way, mux8way16, dmux4way, mux4way16

# Memory has a notion of 'state'.  Memory must maintain state over time.  I used classes for chips with memory instead of 
# just functions to keep track of state

class Bit:
    def __init__(self):
        pass

    def write(self, i, load):
        pass

class Register:
    def __init__(self):
        pass

    def write(self, i, load):
        pass

class RAM8:
    def __init__(self):
        pass

    def write(self, i, load, address):
        pass

class RAM64:
    def __init__(self):
        pass
    
    def write(self, i, load, address):
        pass

class RAM512:
    def __init__(self):
        pass

    def write(self, i, load, address):
        pass

class RAM4K:
    def __init__(self):
        pass
    
    def write(self, i, load, address):
        pass

class RAM16K:
    def __init__(self):
        pass
    
    def write(self, i, load, address):
        pass

class FAST_RAM:
    def __init__(self):
        pass
    
    def write(self, i, load, address):
        pass

class FAST_REGISTER:
    def __init__(self):
        pass
    
    def write(self, i, load):
        pass
