# 21sh

ls ; cat | ls ; ls "tot" "tata et" titi >> super

WORD -  SEPAROTOR_OP -  WORD - 
ls      ;               cat


ls ; ls | ls
ls 

my rules : 
complete_command    : list separator
                    | list

list                : list separator pipe_sequence

pipe_sequence       : command
                    | pipe_sequence '|' linebreak  command




command     : expr
            | expr ; command

expr        : term
            | term '|' expr
            | term (redirection) *

term:       word

separator   : ';'
            | '&'