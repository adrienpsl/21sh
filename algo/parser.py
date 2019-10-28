# here the parser.

# Token types :
#
# EFO is for the last token

# the grammar key word
#
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
 VARIABLE) = (
    'NEWLINE', 'WORD', 'IO_NUMBER', 'PIPE', 'LESS', 'GREAT', 'LESSAND',
    'GREATAND', 'DGREAT', 'VARIABLE'
)

# here the parser : will delete the "" and ''
# put the $ in variable,
# cut the other command in stuff,
# but the " $titi " super ... it's just a word, after that word, I will
# yep, that "" will be a word and I will reaplace the stuff after the word will be
# created

#  \n 
# DLESS, LESSGREAT, CLOBBER, SEMI, DLESS, DLESSDASH) = ()


# ici je ne comprends pas comment faire pour avoir ce truc bonien impel
# lementer, 1 je separe les tokens en ?

#  the func that will go on the line
#  the func that will create the token
#  the function that will
#  pour le moment, je ne retourn que des tokens, operator, and
#  bon la j'ai compris comment faire pour que ce soit plus lisible !
#  youhou.
