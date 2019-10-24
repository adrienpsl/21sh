Bang : !

%token  DLESS  DGREAT  LESSAND  GREATAND  LESSGREAT  DLESSDASH
/*      '<<'   '>>'    '<&'     '>&'      '<>'       '<<-'   */

complete_command    : list separator
                    | list

list                : list separator_op and_or
                    | and_or
                    
and_or              :                   pipeline
                    | and_or linebreak  pipeline

pipe_sequence       : command
                    | pipe_sequence '|' linebreak command

command             : simple_command
                    | compound_command
                    | compound_command      redirect_list
                    | function_definition

subshell            : '(' coumpound_list ')'

compound_list       :               term
                    | newline_list  term
                    |               term     separator
                    | newline_list  term     separator

term                : term separator and_or
                    | and_or

simple_command      : cmd_prefix cmd_word   cmd_suffix
                    | cmd_prefix cmd_word
                    | cmd_prefix
                    | cmd_name              cmd_suffix
                    | cmd_name

cmd_name            : WORD

cmd_word            : WORD

cmd_suffix          :               io_redirect
                    | cmd_suffix    io_redirect
                    |               WORD
                    | cmd_suffix    WORD

redirect_list       :               io_redirect
                    | redirect_list io_redirect

io_redirect         :           io_file
                    | IO_NUMBER io_file
                    |           io_here
                    | IO_NUMBER io_here

io_file             : '<'       filename
                    | LESSAND   filename
                    | '>'       filename
                    | GREATAND  filename
                    | DGREAT    filename
                    | LESSGREAT filename
                    | CLOBBER   filename
                    
filename            : WORD

io_here             : DLESS     here_end
                    | DLESSDASH here_end