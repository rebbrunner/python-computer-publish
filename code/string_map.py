# A class for building all the numerical representations of keyboard characters

class StringMap:
    def __init__(self):
        self.map = {}
        
        count = 65

        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.map[f'{char}'] = count
            count += 1
        
        self.map[' '] = 32
        self.map[':'] = 58
        self.map['?'] = 63
        self.map[';'] = 59
        
        count = 48

        for char in '0123456789':
            self.map[f'{char}'] = count
            count += 1
