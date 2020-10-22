import ipdb
import sys
from antlr4 import *
from Java9Lexer import Java9Lexer
from Java9Parser import Java9Parser
from test.Cobol85Parser import Cobol85Parser 
from test.Cobol85Lexer import Cobol85Lexer
from test.Cobol85PreprocessorParser import Cobol85PreprocessorParser
from test.Cobol85PreprocessorLexer import Cobol85PreprocessorLexer


def parseCobolPreCompiler(argv):
    input_stream = FileStream(argv[1])
    lexer = Cobol85PreprocessorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85PreprocessorParser(stream)
    # tree = parser.query()
    tree = parser.compilationUnit()
    print(tree)    


def parseCobol(argv):
    input_stream = FileStream(argv[1])
    lexer = Cobol85Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)
    # tree = parser.query()
    tree = parser.compilationUnit()
    print(tree)
    # ipdb.set_trace()


def main(argv):
    parseCobolPreCompiler(argv)


 
if __name__ == '__main__':
    main(sys.argv)