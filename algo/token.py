(COMPLETE_COMMAND, LIST, PIPE, CMD, CMD_NAME,
 CMD_WORD, CMD_PREFIX, CMD_SUFFIX, REDIRECT_LIST,
 IO_REDIRECT, IO_FILE, FILENAME, HERE_END, NEWLINE_LIST,
 LINEBREAK, SEPARATOR_OP, SEPARATOR, SEQUENTIAL_SEP, EFO) = (
    'COMPLETE_COMMAND', 'LIST', 'PIPE', 'CMD', 'CMD_NAME',
    'CMD_WORD', 'CMD_PREFIX', 'CMD_SUFFIX', 'REDIRECT_LIST',
    'IO_REDIRECT', 'IO_FILE', 'FILENAME', 'HERE_END', 'NEWLINE_LIST',
    'LINEBREAK', 'SEPARATOR_OP', 'SEPARATOR', 'SEQUENTIAL_SEP', 'EFO')

# the tokon keyword
(NEWLINE, WORD, IO_NUMBER, PIPE, LESS, GREAT, LESSAND, GREATAND, DGREAT,
 VARIABLE, DLESS, DLESS) = (
    '\n', 'WORD', 'IO_NUMBER', '|', '<', '>', '<&',
    '>&', '>>', 'VARIABLE', '<<', '<<-'
)


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    # this method is call when print() or str() is invoked on an object,
    # the method must return a string object.
    # 
    def __str__(self):
        """string representation of the class instance"""
        return 'Token ({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    # here I return str if repr is call, as repr must return str, that makes
    # sens
    def __repr__(self):
        return self.__str__()
