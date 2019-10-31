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
            if self.token.type == OPERATOR:
                self.token.type = OPERATORS.get(self.token.value).type
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

    # if token == Operator && token.value + char == new token
    # that will also handle the \n
    def rule_2(self):
        if self.quote is None \
                and self.token.type == OPERATOR \
                and self.is_operator(self.token.value + self.char):
            self.token.value += self.char
            return 1
        return 0

    # create the operator token
    # that will also handle the \n
    def rule_3(self):
        if self.is_operator(self.char) and self.quote is None:
            self.add_token()
            self.token.type = OPERATOR
            self.token.value += self.char
            return 1
        return 0

    # delimit the token if current char == ' '
    # skip all next ' ' in the string.
    def rule_8(self):
        if self.quote is None and self.char == " ":
            self.add_token()
            while self.next_char() == " ":
                self.advance()
            return 1
        return 0

    def rule_11(self):
        if self.token.type != WORD:
            self.add_token()
        if self.token.type == WORD and self.char:
            self.token.value += self.char
        else:
            self.token.type = WORD
            self.token.value = self.char

    def rule_backslash(self):
        if self.quote is not None and self.char == "\\":
            if self.quote == '"' and self.next_char() == '"':
                self.advance()
                return 1
            if self.quote == "'" and self.next_char() == "'":
                self.advance()
                return 1
        return 0

    # set the quote and unset the quote mode
    def rule_4(self):
        if self.quote is None and (self.char == "\"" or self.char == '\''):
            self.quote = self.char
            return 1
        if self.char == self.quote:
            self.quote = None
            return 1
        self.rule_backslash()
        return 0

    def get_next_token(self):
        while self.advance() and self.char is not None:
            if self.rule_2():
                continue
            if self.rule_3():
                continue
            if self.rule_4():
                continue
            if self.rule_8():
                continue
            if self.rule_11():
                continue

        if self.token.type != NEW:
            self.add_token()
        self.all_tokens.append(MyToken(EFO, "toto"))
