// Grammar.g4
grammar Grammar;

// Parser rules
program: stateDefinition EOF;

stateDefinition
    : entryMark? STATE? symbol=IDENTIFIER (namedAs)? LBRACE stateBody RBRACE
    | entryMark? STATE? symbol=IDENTIFIER (namedAs)? SEMICOLON
    ;

entryMark
    : 'entry'
    | ARROW
    ;

namedAs
    : AS STRING
    ;

stateBody
    : statement*
    ;

statement
    : stateDefinition
    | transitionStatement
    | SEMICOLON
    ;

transitionStatement
    : (fromSymbol=IDENTIFIER)? ARROW toSymbol=IDENTIFIER COLON eventList (backwardDef)? SEMICOLON
    ;

eventList
    : event (PLUS event)*
    ;

event
    : IDENTIFIER
    ;

backwardDef
    : LPAREN CARET INTEGER RPAREN
    ;

// Lexer rules
STATE: 'state';
AS: 'as';
ARROW: '->';
PLUS: '+';
CARET: '^';
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
COLON: ':';
SEMICOLON: ';';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
INTEGER: [0-9]+;

STRING
    : '"' (~["\\\r\n] | EscapeSequence)* '"'
    | '\'' (~['\\\r\n] | EscapeSequence)* '\''
    ;

fragment EscapeSequence
    : '\\' [btnfr"'\\]
    | '\\' ([0-3]? [0-7])? [0-7]
    | '\\' 'u' HexDigit HexDigit HexDigit HexDigit
    | '\\' 'x' HexDigit HexDigit
    ;

fragment HexDigit
    : [0-9a-fA-F]
    ;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
PYTHON_COMMENT: '#' ~[\r\n]* -> skip;

WS: [ \t\r\n]+ -> skip;
