from token import *
from define import *

OPERATOR = 0
TOKEN = 1


class Lexer(object):
    def __init__(self, text):
        # the all command
        self.text = text
        # size of the command
        self.text_length = len(self.text) - 1
        # current pos in the command
        self.pos = 0
        self.current_char = None
        self.current_token = ""
        self.current_token_type = 0

    def is_current_token_operator(self, token: Token):
        tmp_token = self.current_token + self.current_char
        return 0 == cmp(tmp_token, token.value)

    # return if the current token is an op
    # loop on the token array, and return true
    # if the current_str + current_char == existing token
    # return the index of the first matched operator.
    def find_operator_token_index(self) -> int:
        i: int = 0
        while i < len(ALL_OPERATOR):
            if self.is_current_token_operator(ALL_OPERATOR[i]):
                return i
        else:
            return -1

    # that will apply the rules 2 and 3 (if no quoting) :
    # if current_token + current_char == Operator: add and return 1
    # I can, the caller will call it only if the current element is already a token
    def add_to_operator_or_delimit(self):
        token = self.find_operator_token_index()
        if token is not -1:
            self.current_token += self.current_char
            return 1
        else:
            self.create_token()
            return 0

    def create_token(self):
        if self.current_token_type == OPERATOR:
            token = self.find_operator_token_index()
            # add it the the token array
        elif self.current_token_type == WORD:
            pass
        elif self.current_token_type == IO_token:
            # convert to int and pass
            pass

    def error(self):
        raise Exception('Lexer bad char')

    def advance(self):
        """ advance the pos ptr, and set the current char """
        self.pos += 1
        if self.pos == self.length:
            self.current_char = None  # indicate the end of the input
        else:
            self.current_char = self.text[self.pos]

    # implemente rule n=1 : return end at the end :)
    def next_char(self):
        next_pos = self.pos + 1
        if next_pos >= self.text_length:
            return None
        else:
            return self.text[next_pos]

    # test rule n=2, pas de quote : current_token == operator && current token +
    # current == op > add

    def skip_space(self):
        while self.current_char == ' ':
            self.advance()
