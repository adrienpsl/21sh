from algo.lexer import *

def main():
    text = ";       222 "

    # print(not toto[0:])
    lexer = Lexer2(text)
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
