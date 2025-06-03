// Grammar.g4
grammar Grammar;

// Parser rules
program: stateDefinition EOF;

stateDefinition
    : STATE symbol=IDENTIFIER (namedAs)? LBRACE stateBody RBRACE
    | IDENTIFIER (namedAs)? LBRACE stateBody RBRACE
    ;

namedAs
    : NAMED STRING
    | AS STRING
    ;

stateBody
    : (entryStatement | stateDefinition | transitionStatement)*
    ;

entryStatement
    : ENTRY symbol=IDENTIFIER SEMICOLON
    | ARROW symbol=IDENTIFIER SEMICOLON
    ;

transitionStatement
    : fromSymbol=IDENTIFIER ARROW toSymbol=IDENTIFIER COLON eventList (backwardDef)? SEMICOLON
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
NAMED: 'named';
AS: 'as';
ENTRY: 'entry';
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
