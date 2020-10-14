import sys
from antlr4 import *
from Java9Lexer import Java9Lexer
from Java9Parser import Java9Parser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Java9Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Java9Parser(stream)
    tree = parser.getParseListeners()
    print(tree)
 
if __name__ == '__main__':
    main(sys.argv)