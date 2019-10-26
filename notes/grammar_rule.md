aclavel



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

### 3.1.2.2 Single quote
Enclosing characters in single quotes preserve the literal value of each
character within the quote.

### 3.1.2.3 Double quote
Enclosing characters in double quotes preserve the literal value of all characters
within the quotes apart with:
* $, `, \ and ! when history expansion
 

// maybe I write that in python and use the same stuff than use in the article 
I read to do the same ! 
yeah! definitely the right way ! 

the main rules of tokening
- the 'newline' shall be returned as the token identifier NEWLINE
- if the token is an operator, the token identifier for that operator shall result
- if the string consist solely (uniquement) of digits and the delimiter is one of '<' or '>', 
  the token identifier IO_NUMBER shall be return 
- Otherwise the token identifier TOKEN result
