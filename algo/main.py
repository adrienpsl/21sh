from algo.lexer import *


def main():
    text = ";;;;toto et >>; \\\" 2&>1     222 "
    text = ">& 1 >><<<><}{2ooe \\\" 'super tata' "
    text = ">& 1 >><<<><}{2ooe  '\\\"  super tata   '  2>&1 2 " \
           ">>& 1 \" tit ti \" "
    # text = "\" \\\"toto \""
    # text = "'super tata' "

    # print(not][ toto[0:])
    lexer = Lexer(text)
    lexer.get_next_token()
    for el in lexer.all_tokens:
        print(el)

    # for element in lexer.all_token:
    #     print(element)
    # parser = Parser(lexer)
    # interpreter = Interpreter(parser)
    # result = interpreter.interpret()
    # print(interpreter.GLOBAL_SCOPE)


if __name__ == '__main__':
    main()
