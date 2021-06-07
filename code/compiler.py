import os

from syntax_analysis import Parser

# Currently the compiler outputs only to xml
# Default path is the programs folder
# Can take a filename or a folder name

class Compiler:   
    def folder_or_filename(self, filename):
        if os.path.isfile(filename):
            self.compile(filename)
        elif os.path.isdir(filename):
            for f in os.listdir(filename):
                _, ext = os.path.splitext(f)
                if ext == '.jack':
                    self.compile(f'{filename}/{f}')
    
    def compile(self, fi):
        fname, ext = os.path.splitext(fi)
        fo = fname + '.vm'
        parser = Parser(fi, fo)
        parser.recursive_descent()

if __name__ == '__main__':
    i = './programs'
    compiler = Compiler()
    compiler.folder_or_filename(i)
