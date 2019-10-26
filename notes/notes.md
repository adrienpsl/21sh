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



