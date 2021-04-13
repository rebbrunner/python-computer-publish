import os

from syntax_analysis import Parser

# Currently the compiler outputs only to xml
# Default path is the programs folder
# Can take a filename or a folder name

class Compiler:   
    def folder_or_filename(self, filename):
        pass
    
    def compile(self, fi):
        pass

if __name__ == '__main__':
    i = './programs'
    compiler = Compiler()
    compiler.folder_or_filename(i)
