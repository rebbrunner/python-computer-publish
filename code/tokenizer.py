import re

# Lexical analysis - Breaks input stream into tokens based on regex expressions

class Tokenizer:
    def __init__(self, filename):
        pass
    
    def tokenize(self):
        pass
    
    def has_more_tokens(self):
        pass
    
    def advance(self):
        pass
    
    def token_type(self):
        pass
    
    def keyword(self):
        pass
    
    def symbol(self):
        pass
    
    def identifier(self):
       pass
    
    def int_val(self):
        pass
    
    def string_val(self):
        pass

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('in_file')
    args = parser.parse_args()
    i = args.in_file

    tokenizer = Tokenizer(i)
    tokenizer.tokenize()
    while tokenizer.has_more_tokens():
        tokenizer.advance()
        if tokenizer.token_type() == 'strinConstant':
            print(tokenizer.string_val())
