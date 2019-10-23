aclavel

# see after 
// show how parse the '' and "" and more. 
https://stackoverflow.com/questions/6697753/difference-between-single-and-double-quotes-in-bash


# Back to the basic, the fucking shell : that what's it does:
The shell is a command language interpreter, the shell operates according to that :
1. the shell reads input.
2. the shell breaks the input into tokens: words and operator : Token Recognition
3. the shell parses the input into simple commands, and compound_commands.
4. the shell parse the input into simple command and compound_commands.
5. the shell performs redirections and removes redirection operator and their operands
6. the shell launch that function
7 the shell wait the end an catch the result.




# The grammar rules: 

## 9.3 History Expansion (https://www.gnu.org/software/bash/manual/html_node/History-Interaction.html)
- History introduce words from the history list into the input stream:
    * History expansion is perform immediately after a complete line is read, before
      the shell breaks into word. And is performed on each line individually.
    * the history expansion takes place in two part: 
        ** the first is to determine which line from the history list should be used.
        ** the second is to select portions of that line for inclusion into the current one.
- The line selected from the history is the called the event and the portions is called words.
  the event is broken into words in the same fashion that Bash does, like 'toto tata' = 1 word

### string interpolation
In computer science, it's the process of evaluating a string literal containing 
place holder, and and yielding a result in which the placeholder are replaced 
with their corresponding value.

## 2.2 Quoting
is used to remove special meaning of certain char or words to the shell.
it can be used to preserve the literal meaning of special char in the next paragraph
or preserve parameter expansion an command substitution.
- all these char need to be quote : 
  |  &  ;  <  >  (  )  $  `  \  "  '  <space>  <tab>  <newline>
these only on certain circumstances :
  *   ?   [   #   ˜   =   %




## 3.1.2.2 Single quote
Enclosing characters in single quotes preserve the literal value of each
character within the quote.

## 3.1.2.3 Double quote
Enclosing characters in double quotes preserve the literal value of all characters
within the quotes apart with:
* $, `, \ and ! when history expansion


## 2.3 Token Recognition

- the shell read its input in term of unlimited length line.
- they can come from a terminal (interactive mode) or a form string : sh -c / system()
  * The function : system()
    ```C99
        #include <stdlib.h>
        int system(const char *command);
    ```
  * The shell command : sh -c 
    ```shell script
    sh -c # the command 
    ```
- These input lines shall be parsed using two major modes:
    
    * processing of here-document :
        ** Grammar rule : ` (DLESS | DLESSDASH) WORD `.
        ** Example :
            `[n] << WORD
                here-document
            delimiter`.
        ** if no n is supply, std in is used
        **  If there is ` ' ` | ` " ` in the WORD, a quote> is set is need
            and no expansion will be activated
        **  the bash man say I do not expand the "" in she here-doc, but zsh do, so I will
        ** remember to delete the start tab if <<- i- provided
    
    * ordinary token recognition :
        - the shell, break its input by applying the first rule below to the next char in the input.
        - the taken shall be from the current position in the input, until a toke is delimited.
        - the characters forming the token are exactly those in the input, including any quoting character.
        - ?? if it's indicated that a token is delimited and no characters have been included in a token
             processing shall continue until an actual token is delimited

not that's is for delemited a token, after that I parse it ! 
### the rules (that only for determine the token, not grammar rules here, I will do that to start the tokenisation ?):
1. if the end of input is recognized, the current token shall be delimited.
   if there is no current token, the end of input indicator shall be returned as token.
2. if teh previous char was used as operator and the current one is also a part of an operator,
   the current one shall be use as the same operator
3. if the previous char was used as part of an operator and the current char cannot be used with the current
   char to form an operator, the operator containing the previous char shall be delimited (is for that, we need the space.!) 
4.  if the current char is backslash, single / double quote, and not quoted,. It shall affect quoting for subsequent char up to 
    the end of the quoted text. During token recognition no substitutions shall be actually performed, and the result token
    shall contain exactly the char that appear in the input (except for the new line), unmodified, including any embedded or 
    enclosing quotes or substitution operator. between the quote mark and the end of the quoted text.
    the token shall not be delimited by the end of the quoted field ??
    - car je peux avoir ls "toto" tata titi et ces command font partie d'un token, et ne doivent donc pas etre changer de place.  
5. If the current caharcer is an unquoted '$' or  '`', the shell identify the start of any candidates for parameter expansion
   rewrite the rule 5 with the new shell, not now.
   
6.  if the current charactere is not quoted and can be used as the first char of a new
    operator, the current token (if any) shall be delimited and the current token shall be used as begging of the next token. (><) ?
7. if the current char is an unquoted <newline>, the cerrunt token shall be delimited.
8. if the current character is an unquoted <blank>, any token containing the previous char
 



>> > << < | and command. 

// maybe I write that in python and use the same stuff than use in the article 
I read to do the same ! 
yeah! definitely the right way ! 

the main rules of tokening
- the 'newline' shall be returned as the token identifier NEWLINE
- if the token is an operator, the token identifier for that operator shall result
- if the string consist solely (uniquement) of digits and the delimiter is one of '<' or '>', 
  the token identifier IO_NUMBER shall be return 
- Otherwise the token identifier TOKEN result

 


she backslash :
-  

Bang : !

%token  DLESS  DGREAT  LESSAND  GREATAND  LESSGREAT  DLESSDASH
/*      '<<'   '>>'    '<&'     '>&'      '<>'       '<<-'   */

## 
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