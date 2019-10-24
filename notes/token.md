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
8. if the current character is an unquoted <blank>, the previous token is delimited, and 
    the current token is done.
9. If the previous character was part of a word, the current character shall be append to that word
10. if the token in an # all the char after it until I get a new_line, are comment,
   the new line that end the line is not considered part of the comment.

// je pense que ici ca me demande de faire des tests pour voir si tout est correct,
// avant de lance la creation de l'ast qui est plus complex en resource ?

1. si c'est la fin de la line: 
    si current token -> done
    si rien -> creation token EOF
2. Si pas de quote, si Ct == operator && Ct + Cc == operator
    j'ajoute le char a mon token
3. Si Ct == operator && Ct + Cc != operator
    le Ct est delimité
4. If the Cc est un \ " ', et n'est pas quoted, je dois set l'option, is quoted,
    mais : 
    - pas de substitution
    - je met tout les char dans le token, et je ne l'arrete pas a la fin du la string, 
        il y a peu etre d'autre chose dedant !
5. 

