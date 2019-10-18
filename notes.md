il faut voir le shell comme un language de programation.
la syntax dois repondre a une grammaire
la semantique specifie la signification d'un programme valide
----
Ce programme est-il valide ? (syntaxe)
Si oui, que fait-il ? (sémantique)


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


les links utiliser :

http://michel.billaud3.free.fr/blog/index.php/2013/01/20/72-programmation-la-technique-de-descente-recursive
https://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html
https://dev.to/oyagci/generating-a-parse-tree-from-a-shell-grammar-f1
https://leptinerd.wordpress.com/2017/06/11/introduction-a-la-theorie-de-la-compilation-24-les-parsers/
https://totodu.net/Compilation/Introduction

https://ruslanspivak.com/lsbasi-part1/
http://gallium.inria.fr/~maranget/X/compil/poly/poly003.html#sec4
https://pubs.opengroup.org/onlinepubs/9699919799/


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
