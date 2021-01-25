# The CodeWriter actually generates asembly code and writes it to file
# Many operations are very similar to each other.  Room for future optimizations
# For operations that branch (eq, gt, lt) a counter is used to gurantee uniqueness

class CodeWriter:
    def __init__(self):
        pass

    def set_filename(self, filename):
        pass

    def add(self):
        pass

    def sub(self):
        pass

    def neg(self):
        pass

    def eq(self):
        pass

    def gt(self):
        pass

    def lt(self):
        pass

    def bitand(self):
        pass

    def bitor(self):
        pass

    def bitnot(self):
        pass

    def write_arithmetic(self, command):
        pass
    
    def push_constant(self, index):
        pass
    
    def push_local(self, index):
        pass
    
    def push_arg(self, index):
        pass
    
    def push_this(self, index):
        pass
    
    def push_that(self, index):
        pass
    
    def push_temp(self, index):
        pass
    
    def push_pointer(self, index):
        pass
    
    def push_static(self, index):
        pass

    def pop_local(self, index):
        pass
    
    def pop_arg(self, index):
        pass
    
    def pop_this(self, index):
        pass
    
    def pop_that(self, index):
        pass

    def pop_temp(self, index):
        pass

    def pop_pointer(self, index):
        pass
    
    def pop_static(self, index):
        pass

    def write_push_pop(self, command, segment, index):
        pass
    
    def close(self):
        pass
