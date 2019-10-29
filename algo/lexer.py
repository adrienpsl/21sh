from filecmp import cmp
from algo.define import *
from algo.myToken import MyToken

ALL_OPERATOR = (
    MyToken(NEWLINE, '\n'), MyToken(PIPE, '|'), MyToken(LESS, '<'),
    MyToken(GREAT, '>'), MyToken(LESSAND, '<&'), MyToken(GREATAND, '>&'),
    MyToken(DGREAT, '>>'), MyToken(LESSAND, '<<'), MyToken(DLESSDASH, '<<-'),
    MyToken(SEMI, ';'))

OPERATOR = 0
MY_TOKEN = 1
WORD = 2
IO_TOKEN = 3


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
        self.all_token = []

    def is_current_token_operator(self, token: MyToken):
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

    def add_current_char(self, token_type):
        self.current_token += self.current_char
        self.current_token_type = token_type

    # that will apply the rules 2 and 3 (if no quoting) :
    # if current_token + current_char == Operator: add and return 1
    # I can, the caller will call it only if the current element
    # is already a token
    def current_is_token(self):
        token = self.find_operator_token_index()
        if token is not -1:
            if self.current_token_type != OPERATOR:
                self.create_token()
            self.add_current_char(OPERATOR)
            return 1
        return 0

    def handle_word(self):
        if self.current_token_type != WORD:
            self.create_token()
        self.add_current_char(WORD)

    def handle_space(self):
        if self.current_char == ' ':
            self.create_token()

    def handle_quote(self):
        # if quote, save the current quote,
        # loop on the element until I get the next quote
        # the delete the quote at each limit
        # save create a word
        pass

    def create_token(self):
        if self.current_token_type == OPERATOR:
            token_index = self.find_operator_token_index()
            self.all_token.append(ALL_OPERATOR[token_index])
            # add it the the token array
        elif self.current_token_type == WORD:
            token = MyToken(WORD, self.current_token)
            self.all_token.append(token)
        elif self.current_token_type == IO_TOKEN:
            # convert to int and pass
            pass
        self.current_token = ""

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
    # imlement <<- and blank.

    def skip_space(self):
        while self.current_char == ' ':
            self.advance()

    def run(self):
        while self.current_char is not None:
            self.advance()
            if self.current_char is None:
                break
            if self.current_is_token():
                continue
            self.handle_word()
            self.handle_space()
        for element in self.all_token:
            print(element)
