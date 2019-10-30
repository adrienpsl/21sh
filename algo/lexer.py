from algo.define import *
from algo.myToken import MyToken

OPERATORS = {
    '\n': MyToken(NEWLINE, '\n'),
    '|': MyToken(PIPE, '|'),
    '<': MyToken(LESS, '<'),
    '>': MyToken(GREAT, '>'),
    '<&': MyToken(LESSAND, '<&'),
    '>&': MyToken(GREATAND, '>&'),
    '<>': MyToken(LESSGREAT, '<>'),
    '>>': MyToken(DGREAT, '>>'),
    '<<': MyToken(LESSAND, '<<'),
    '<<-': MyToken(DLESSDASH, '<<-'),
    ';': MyToken(SEMI, ';')
}

OPERATOR = "OP"
MY_TOKEN = "MY_TOKEN"
WORD = "WORD"
IO_TOKEN = "IO_TOKEN"
NEW = "NEW"


class Lexer2(object):
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.char = text[0]
        self.token = self.fresh_token()
        self.all_tokens = []
        self.quote = None

    @staticmethod
    def fresh_token():
        return MyToken(NEW, "")

    @staticmethod
    def is_operator(current_char):
        return OPERATORS.get(current_char, None)

    def add_token(self):
        if self.token.type != NEW:
            self.all_tokens.append(self.token)
            self.token = self.fresh_token()

    def error(self):
        raise Exception('bad Lexer char')

    def advance(self):
        self.char = \
            self.text[0] if self.text else None
        self.text = self.text[1:]
        return 1

    def next_char(self):
        return self.text[0] if self.text else None

    # delimit the token if current char == ' '
    # skip all next ' ' in the string.
    def rule_8(self):
        self.add_token()

    def rule_11(self):
        if self.token.type != WORD:
            self.add_token()
        if self.token.type == WORD:
            self.token.value += self.char
        else:
            self.token.type = WORD
            self.token.value = self.char

    # if token == Operator && token.value + char == new token
    # that will also handle the \n
    def rule_2(self):
        if self.token.type == OPERATOR and self.is_operator(
                self.token.value + self.char):
            self.token.value += self.char
            return 1
        return 0

    # create the operator token
    # that will also handle the \n
    def rule_3(self):
        if self.is_operator(self.char):
            self.add_token()
            self.token.type = OPERATOR
            self.token.value += self.char
            return 1
        return 0

    def add_the_quote(self):
        self.advance()
        self.rule_11()

    def handle_backslash(self):
        if self.char == "\\" and self.quote:
            if self.quote == '"' and self.next_char() == '"':
                self.add_the_quote()
                return 1
            if self.quote == "'" and self.next_char() == "'":
                self.add_the_quote()
                return 1
        return 0

    def rule_4(self):
        if self.char == "\"" or self.char == "'":
            self.quote = self.char
            self.advance()
            while self.char != self.quote:
                self.handle_backslash()
                self.rule_11()
                self.advance()
            return 1
        return 0

    def get_next_token(self):
        while self.advance() and self.char is not None:
            if self.rule_2():
                continue
            if self.rule_3():
                continue
            if self.rule_4():
                continue
            if self.char == ' ':
                self.rule_8()
                continue
            if self.rule_11():
                continue

        if self.token.type != NEW:
            self.add_token()
        self.all_tokens.append(MyToken(EFO, "toto"))
