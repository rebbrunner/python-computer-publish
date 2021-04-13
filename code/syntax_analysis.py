from tokenizer import Tokenizer

# Syntax Analysis - Recursive descent parser
# First stage - outputs to xml the parse tree

class Parser:
    def __init__(self, fi, fo):
        pass
    
    def write(self):
        pass

    def recursive_descent(self):
        pass
    
    def descend_into_class(self):
        pass
    
    def descend_into_class_var_dec(self):
        pass
    
    def descend_into_subroutine_dec(self):
        pass
    
    def descend_into_param_list(self):
        pass
    
    def descend_into_subroutine_body(self):
        pass
    
    def descend_into_var_dec(self):
        pass
    
    def descend_into_statements(self):
        pass
    
    def descend_into_let_statement(self):
        pass
    
    def descend_into_do_statement(self):
        pass

    def descend_into_while_statement(self):
        pass

    def descend_into_if_statement(self):
        pass

    def descend_into_return_statement(self):
        pass

    def descend_into_subroutine_call(self):
        pass

    def descend_into_expression_list(self):
        pass

    def descend_into_expression(self):
        pass
    
    def descend_into_term(self):
        pass

if __name__ == '__main__':
    i = './programs/Main.jack'
    o = './programs/Main.xml'
    parser = Parser(i, o)
    parser.recursive_descent()
