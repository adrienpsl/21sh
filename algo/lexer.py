from algo.token import *
from algo.define import *


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

    # // TODO : how cmp str in python ?
    def is_current_token_operator(self, token: Token):
        tmp_token = self.current_token + self.current_char
        return tmp_token == token.value

    # return if the current token is an op
    # loop on the token array, and return true
    # if the current_str + current_char == existing token
    def is_op(self):
        for element in ALL_OPERATOR:
            if self.is_current_token_operator(element):
                return element
        else:
            return None

    # that will apply the rules 2 and 3 (works if no quoting) :
    # si
    def add_to_operator_or_delimit(self):
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
