# see after 
// show how parse the '' and "" and more. 
https://stackoverflow.com/questions/6697753/difference-between-single-and-double-quotes-in-bash


c'est ce que je dois implementer, dans cet ordre.
# Back to the basic, the fucking shell : that what's it does:
The shell is a command language interpreter, the shell operates according to that :
1. the shell reads input.
2. the shell breaks the input into tokens: words and operator : Token Recognition
3. the shell parses the input into simple commands, and compound_commands.
4. the shell parse the input into simple command and compound_commands.
5. the shell performs redirections and removes redirection operator and their operands
6. the shell launch that function
7 the shell wait the end an catch the result.


>> > << < | and command.




# Analyse lexical

## Le lexer 
je dois gererer un arbre qui represente ce que j'ai avec mes element,
pour faire un truc compilable
donc surtout annalyser ce que je recois dans mon shell, et
ensuite lancer les executions.
- les tokens exploitables sont : 
';' '|' ; '<' '>' '<<' '>>' les descripeurs de file. 

je commence a comprendre ce que je dois faire avec le lexer, et ensuite avec 
le parser. 

mais comment faire pour que tout se plug correctement ?



# https://ruslanspivak.com/lsbasi-part1/
## Part 1

### 1. What is an interpreter
on interpreter, will only interpret the source code.

### 2. What is a compiler 
The compiler translate the L1 language into a binary one, 
that will understand by the L2 reader.

### 3. What's the difference between an interpreter and a compiler ?
the compiler translate in a second language, the interpreter run directly

### 4. What is a Token
an structure with a defined type and an value

### 5. What is the name of the process that breaks input apart tokens ?
a lexer, lexical Analyzer / scanner / tokenizer


## Part 2

### 1. What's is a lexeme 
a lexeme is a possible token value like :
- INTEGER = 1,1,3,33,99
- MINUS = '-'

### 2. What's is the name of the process 
parser / parsing

## Part 3
### 1. What's is a syntax diagram ?
It's a graphical diagram of the programing syntax rules.

### 2. What's is a syntax analysis ?
It's the parser, It will check if the rules of the language are respected

## part 9
- part 9 is a start to real stuff man: we will write a pascal compiler ! OMG

## The rules of the Pascal :
- A pascal program consist of a compound statement that end with a dot.
- A compound statement is a block marked with BEGIN and END that contains a list
  (possibly empty) of statement, possibly other compound statement.
  Every statement inside must terminate with a semicolon, except the last one.
  ```pascal
  “BEGIN END”
  “BEGIN a := 5; x := 11 END”
  “BEGIN a := 5; x := 11; END”
  “BEGIN BEGIN a := 5 END; x := 11 END” 
  ```
- A statement list is a list of * statement inside a compound statement
- A assignment statement is a variable followed by an Assign token : (: =)
  followed by an expression.
  ```pascal
  a := 11
  b := a + 9 - 5 * 2
  ```
- A variable is an identifier. We'll use the Id token for variables.
  The value of the variable will be his name.
  ```pascal
  BEGIN a := 11; b := a + 9 - 5 END
  ```
- An empty statement represents a grammar rule with no further productions.
  We use the empty_statement grammar rules to indicate the end of the statement_list
  in the parser, and also to allow for empty compound statements as in 'BEGIN END'.
- the factor ruse is updated to handle variable.

// here an pretty exemple of how handle some cool stuff :

## the rules: 
program            : compound_statement DOT

compound_statement : BEGIN statement_list END

statement_list     : statement
                   | statement SEMI statement_list // best than with the *, cause 2 possibility, different.

statement          : compound_statement
                   | assigment_statement
                   | empty

assignment_statement: variable ASSIGN expr

empty: --

expr: term ((PLUS | MINUS) term)*

term: factor ((MUL | DIV) factor)*

factor: PLUS factor
      | MINUS factor
      | INTEGER
      | LPAREN expr RPAREN
      | variable

variable : ID

## The new parser:
1. To support the pascal language, we need to change the lexer, to return new token :
BEGIN / END : surround the compound_statement
DOT : the .
ASSIGN : 2 char :=
SEMI: used to mark the end of a statement, inside a compound_statement
ID: A token for a valid identifier, identifier start with alphabetical 
followed by any number of alphanumerical char.

2. we add an method to get the next char of the input, without increment pos,
in order to find the token after the := or == =<
the method name is peek.
```python
def peek(self):
    peek_pos = self.pos + 1
    if peek_pos > len(self.text) - 1:
        return None
    else:
        return self.text[peek_pos]
```
Because Pascal variable and reserved keyword are both identifiers,
we will combine their handling into one method called _id.
the method consumes all the alphanumeric, and if it's an 
keyword, return the predefined token, if not, return a new ID token
where the value is an the variable name (lexeme).

## The new grammar : 
program : PROGRAM variable SEMI block DOT

block : declarations compound_statement

declarations : VAR (variable declaration SEMI)+
            | empty

variable_declaration: ID (COMMA ID)* COLON type_spec

type_spec : INTEGER | REAL

compound_statement : BEGIN statement_list END

statement_list : statement
                | statement SEMI statement_list

statement: compound_statement
            | assignment_statement
            | empty
                                (:=) both
assignment_statement : variable ASSIGN expr

empty : --

expr : term ((PLUS | MINUS) term) * 

term : factor ((MUL | DIV) factor) *

factor : PLUS factor
        | MINUS factor
        | INTEGER_CONST
        | REAL_CONST
        | LPAREN expr RPAREN
        | variable

variable : ID

now we want to update the lexer, after the parser, after that the interpreter! youhou !
I think the grammar rules start to enter in my head, that simple, 
but use the parser a descente recusive, that seem to be hard !

















https://linux.die.net/man/2/pipe
https://stackoverflow.com/questions/50610781/implementing-pipe-and-redirection-together-in-c
http://www.zeitoun.net/articles/communication-par-tuyau/start
https://forum.ubuntu-fr.org/viewtopic.php?id=1952491