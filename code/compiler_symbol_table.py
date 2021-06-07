# Symbol table used by compiler for tracking variables.
# Compiler does not support nested functions, so one subroutine table can be recycled
# Compiler only supports one class per file so class table can be recycled

class SymbolTable:
    def __init__(self):
        pass
    
    def start_subroutine(self):
        pass
    
    def define(self, name, dtype, kind):
        pass
    
    def var_count(self, kind):
        pass
    
    def kind_of(self, name):
        pass
    
    def type_of(self, name):
        pass
    
    def index_of(self, name):
        pass

if __name__ == '__main__':
    table = SymbolTable()
    table.define('test', 'String', 'VAR')
    table.define('test1', 'String', 'VAR')
    table.define('test3', 'int', 'VAR')
    table.define('test2', 'String', 'ARG')
    table.define('test', 'String', 'STATIC')
    table.define('test1', 'String', 'STATIC')
    table.define('test2', 'String', 'FIELD')
    table.define('test3', 'String', 'FIELD')
    table.define('test4', 'char', 'FIELD')
    print(table.classtable)
    print(table.subtable)
    print(table.var_count('STATIC'))
    print(table.var_count('FIELD'))
    print(table.var_count('ARG'))
    print(table.var_count('VAR'))
    print(table.kind_of('test3'))
    print(table.kind_of('test4'))
    print(table.type_of('test3'))
    print(table.type_of('test4'))
    print(table.index_of('test3'))
    print(table.index_of('test4'))
