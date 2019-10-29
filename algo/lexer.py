from algo.define import *
from algo.myToken import MyToken

OPERATORS = {
    '\n': MyToken(NEWLINE, '\n'),
    '|': MyToken(PIPE, '|'),
    '<': MyToken(LESS, '<'),
    '>': MyToken(GREAT, '>'),
    '<&': MyToken(LESSAND, '<&'),
    '>&': MyToken(GREATAND, '>&'),
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


# that class containt the current text in the
class Current(object):
    def __init__(self):
        self.current_char = ""
        self.current_string = ""
        self.current_token_type = 0

    # cc == current_char current_string
    def is_cc_and_ct_operator(self):
        return OPERATORS.get(self.current_string + self.current_char, None)

    def is_cc_operator(self):
        return OPERATORS.get(self.current_char)

    def set_current_char(self, token_type):
        if self.current_char is not None:
            self.current_token += self.current_char
            self.current_token_type = token_type
            return 0
        else:
            self.current_token_type = EFO
            return 1


class Lexer2(object):
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.char = text[0]
        self.token = self.fresh_token()
        self.all_tokens = []

    @staticmethod
    def fresh_token():
        return MyToken(NEW, "")

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

    def handle_blank(self):
        self.add_token()

    def add_to_word(self):
        if self.token.type != WORD:
            self.add_token()
        if self.token.type == WORD:
            self.token.value += self.char
        else:
            self.token.type = WORD
            self.token.value = self.char

    def get_next_token(self):
        while self.advance() and self.char is not None:
            if self.char == ' ':
                self.handle_blank()
                continue
            if self.add_to_word():
                continue
        if self.token != NEW:
            self.add_token()
        self.all_tokens.append(MyToken(EFO, "toto"))


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.text_length = len(self.text) - 1
        self.pos = 0
        self.all_token = [],
        self.token = MyToken("", None)
        self.current_char = ""

    # that will apply the rules 2 and 3 (if no quoting) :
    # if current_token + current_char == Operator: add and return 1
    # I can, the caller will call it only if the current element
    # is already a token
    def current_is_token(self, ):
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
            self.skip_space()

    def handle_quote(self):
        # if quote, save the current quote,
        # loop on the element until I get the next quote
        # the delete the quote at each limit
        # save create a word
        pass

    def create_token(self):
        if self.current_token_type == OPERATOR:
            token_index = self.find_operator_token_index()
            self.all_token.append(OPERATORS[token_index])
            # add it the the token array
        elif self.current_token_type == WORD:
            token = MyToken(WORD, self.current_token)
            self.all_token.append(token)
        elif self.current_token_type == IO_TOKEN:
            # convert to int and pass
            pass
        elif self.current_token_type == EFO:
            self.all_token.append(MyToken(EFO, 'stop'))
        # I reset the value
        self.current_token = ""
        self.current_token_type = None

    def error(self):
        raise Exception('Lexer bad char')

    def advance(self):
        """ advance the pos ptr, and set the current char """
        if self.pos > self.text_length:
            self.current_char = None  # indicate the end of the input
        else:
            self.current_char = self.text[self.pos]
        self.pos += 1

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

    def loop_on_way(self):
        if self.current_is_token():
            return True
        if self.handle_space():
            return True
        if self.handle_word():
            return True
        return False

    def run(self):
        # while self.current_char is not None:
        #     self.advance()
        #     if self.current_char is None:
        #         break
        #     self.loop_on_way()
        # self.create_token()
        # for element in self.all_token:
        #     print(element)
        pass
