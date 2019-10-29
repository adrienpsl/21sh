from lexer import *


def main():
    text = "super test"

    lexer = Lexer(text)
    lexer.run()
    # for element in lexer.all_token:
    #     print(element)
    # parser = Parser(lexer)
    # interpreter = Interpreter(parser)
    # result = interpreter.interpret()
    # print(interpreter.GLOBAL_SCOPE)


if __name__ == '__main__':
    main()
