# import all, the . is important.
from token import *

RESERVED_WORD = {
    'BEGIN': Token(WORD, 'toto')
}


class Lexer(object):
    def __init__(self, text):
        # the all command
        self.text = text
        # size of the command
        self.text_length = len(self.text) - 1
        # current pos in the command
        self.pos = 0
        self.current = None

    def error(self):
        raise Exception('Lexer bad char')

    def advance(self):
        """ advance the pos ptr, and set the current char """
        self.pos += 1
        if self.pos == self.length:
            self.current = None  # indicate the end of the input
        else:
            self.current = self.text[self.pos]

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
        while self.current == ' ':
            self.advance()
