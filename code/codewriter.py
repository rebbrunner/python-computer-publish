import os

# Class responsible for writing code to file

class CodeWriter:
    def __init__(self, fname):
        pass

    def write_push(self, seg, index):
        pass

    def write_pop(self, seg, index):
        pass
    
    def write_arithmetic(self, command):
        pass
    
    def write_label(self, label):
        pass
    
    def write_goto(self, label):
        pass
    
    def write_if(self, label):
        pass
    
    def write_call(self, name, nargs):
        pass
    
    def write_function(self, name, nlcl):
        pass
    
    def write_return(self):
        pass
    
    def close(self):
        pass

if __name__ == '__main__':
    o = './programs/program'
    writer = CodeWriter(o)
    writer.write_push('constant', 5)
    writer.write_push('constant', 10)
    writer.write_arithmetic('add')
    writer.write_pop('local', 0)
    writer.write_label('LOOP')
    writer.write_push('constant', 0)
    writer.write_if('LOOP')
    writer.write_call('new', 1)
    writer.write_function('new', 1)
    writer.write_return()
    writer.close()
