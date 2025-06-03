# Generated from ./pylayerstates/dsl/grammar/Grammar.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u00ba\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\7\17Z\n\17\f\17\16\17]\13\17\3\20\6\20`\n\20\r\20")
        buf.write("\16\20a\3\21\3\21\3\21\7\21g\n\21\f\21\16\21j\13\21\3")
        buf.write("\21\3\21\3\21\3\21\7\21p\n\21\f\21\16\21s\13\21\3\21\5")
        buf.write("\21v\n\21\3\22\3\22\3\22\3\22\5\22|\n\22\3\22\5\22\177")
        buf.write("\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u008e\n\22\3\23\3\23\3\24\3\24\3")
        buf.write("\24\3\24\7\24\u0096\n\24\f\24\16\24\u0099\13\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u00a4\n\25")
        buf.write("\f\25\16\25\u00a7\13\25\3\25\3\25\3\26\3\26\7\26\u00ad")
        buf.write("\n\26\f\26\16\26\u00b0\13\26\3\26\3\26\3\27\6\27\u00b5")
        buf.write("\n\27\r\27\16\27\u00b6\3\27\3\27\3\u0097\2\30\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\2%\2'\23)\24+\25-\26\3\2\r\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\3\2\62;\6\2\f\f\17\17$$^^\6\2\f\f\17")
        buf.write("\17))^^\n\2$$))^^ddhhppttvv\3\2\62\65\3\2\629\5\2\62;")
        buf.write('CHch\4\2\f\f\17\17\5\2\13\f\17\17""\2\u00c7\2\3\3\2')
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\3/\3\2\2\2\5\65\3\2\2\2\7;\3")
        buf.write("\2\2\2\t>\3\2\2\2\13D\3\2\2\2\rG\3\2\2\2\17I\3\2\2\2\21")
        buf.write("K\3\2\2\2\23M\3\2\2\2\25O\3\2\2\2\27Q\3\2\2\2\31S\3\2")
        buf.write("\2\2\33U\3\2\2\2\35W\3\2\2\2\37_\3\2\2\2!u\3\2\2\2#\u008d")
        buf.write("\3\2\2\2%\u008f\3\2\2\2'\u0091\3\2\2\2)\u009f\3\2\2\2")
        buf.write("+\u00aa\3\2\2\2-\u00b4\3\2\2\2/\60\7u\2\2\60\61\7v\2\2")
        buf.write("\61\62\7c\2\2\62\63\7v\2\2\63\64\7g\2\2\64\4\3\2\2\2\65")
        buf.write("\66\7p\2\2\66\67\7c\2\2\678\7o\2\289\7g\2\29:\7f\2\2:")
        buf.write("\6\3\2\2\2;<\7c\2\2<=\7u\2\2=\b\3\2\2\2>?\7g\2\2?@\7p")
        buf.write("\2\2@A\7v\2\2AB\7t\2\2BC\7{\2\2C\n\3\2\2\2DE\7/\2\2EF")
        buf.write("\7@\2\2F\f\3\2\2\2GH\7-\2\2H\16\3\2\2\2IJ\7`\2\2J\20\3")
        buf.write("\2\2\2KL\7}\2\2L\22\3\2\2\2MN\7\177\2\2N\24\3\2\2\2OP")
        buf.write("\7*\2\2P\26\3\2\2\2QR\7+\2\2R\30\3\2\2\2ST\7<\2\2T\32")
        buf.write("\3\2\2\2UV\7=\2\2V\34\3\2\2\2W[\t\2\2\2XZ\t\3\2\2YX\3")
        buf.write("\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\36\3\2\2\2][\3")
        buf.write("\2\2\2^`\t\4\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2")
        buf.write("\2b \3\2\2\2ch\7$\2\2dg\n\5\2\2eg\5#\22\2fd\3\2\2\2fe")
        buf.write("\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2ik\3\2\2\2jh\3\2")
        buf.write("\2\2kv\7$\2\2lq\7)\2\2mp\n\6\2\2np\5#\22\2om\3\2\2\2o")
        buf.write("n\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2sq\3")
        buf.write('\2\2\2tv\7)\2\2uc\3\2\2\2ul\3\2\2\2v"\3\2\2\2wx\7^\2')
        buf.write("\2x\u008e\t\7\2\2y~\7^\2\2z|\t\b\2\2{z\3\2\2\2{|\3\2\2")
        buf.write("\2|}\3\2\2\2}\177\t\t\2\2~{\3\2\2\2~\177\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u008e\t\t\2\2\u0081\u0082\7^\2\2\u0082")
        buf.write("\u0083\7w\2\2\u0083\u0084\5%\23\2\u0084\u0085\5%\23\2")
        buf.write("\u0085\u0086\5%\23\2\u0086\u0087\5%\23\2\u0087\u008e\3")
        buf.write("\2\2\2\u0088\u0089\7^\2\2\u0089\u008a\7z\2\2\u008a\u008b")
        buf.write("\5%\23\2\u008b\u008c\5%\23\2\u008c\u008e\3\2\2\2\u008d")
        buf.write("w\3\2\2\2\u008dy\3\2\2\2\u008d\u0081\3\2\2\2\u008d\u0088")
        buf.write("\3\2\2\2\u008e$\3\2\2\2\u008f\u0090\t\n\2\2\u0090&\3\2")
        buf.write("\2\2\u0091\u0092\7\61\2\2\u0092\u0093\7,\2\2\u0093\u0097")
        buf.write("\3\2\2\2\u0094\u0096\13\2\2\2\u0095\u0094\3\2\2\2\u0096")
        buf.write("\u0099\3\2\2\2\u0097\u0098\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b\7")
        buf.write(",\2\2\u009b\u009c\7\61\2\2\u009c\u009d\3\2\2\2\u009d\u009e")
        buf.write("\b\24\2\2\u009e(\3\2\2\2\u009f\u00a0\7\61\2\2\u00a0\u00a1")
        buf.write("\7\61\2\2\u00a1\u00a5\3\2\2\2\u00a2\u00a4\n\13\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3")
        buf.write("\2\2\2\u00a8\u00a9\b\25\2\2\u00a9*\3\2\2\2\u00aa\u00ae")
        buf.write("\7%\2\2\u00ab\u00ad\n\13\2\2\u00ac\u00ab\3\2\2\2\u00ad")
        buf.write("\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\u00b1\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2\b")
        buf.write("\26\2\2\u00b2,\3\2\2\2\u00b3\u00b5\t\f\2\2\u00b4\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\b\27\2")
        buf.write("\2\u00b9.\3\2\2\2\21\2[afhoqu{~\u008d\u0097\u00a5\u00ae")
        buf.write("\u00b6\3\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    STATE = 1
    NAMED = 2
    AS = 3
    ENTRY = 4
    ARROW = 5
    PLUS = 6
    CARET = 7
    LBRACE = 8
    RBRACE = 9
    LPAREN = 10
    RPAREN = 11
    COLON = 12
    SEMICOLON = 13
    IDENTIFIER = 14
    INTEGER = 15
    STRING = 16
    BLOCK_COMMENT = 17
    LINE_COMMENT = 18
    PYTHON_COMMENT = 19
    WS = 20

    channelNames = ["DEFAULT_TOKEN_CHANNEL", "HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = [
        "<INVALID>",
        "'state'",
        "'named'",
        "'as'",
        "'entry'",
        "'->'",
        "'+'",
        "'^'",
        "'{'",
        "'}'",
        "'('",
        "')'",
        "':'",
        "';'",
    ]

    symbolicNames = [
        "<INVALID>",
        "STATE",
        "NAMED",
        "AS",
        "ENTRY",
        "ARROW",
        "PLUS",
        "CARET",
        "LBRACE",
        "RBRACE",
        "LPAREN",
        "RPAREN",
        "COLON",
        "SEMICOLON",
        "IDENTIFIER",
        "INTEGER",
        "STRING",
        "BLOCK_COMMENT",
        "LINE_COMMENT",
        "PYTHON_COMMENT",
        "WS",
    ]

    ruleNames = [
        "STATE",
        "NAMED",
        "AS",
        "ENTRY",
        "ARROW",
        "PLUS",
        "CARET",
        "LBRACE",
        "RBRACE",
        "LPAREN",
        "RPAREN",
        "COLON",
        "SEMICOLON",
        "IDENTIFIER",
        "INTEGER",
        "STRING",
        "EscapeSequence",
        "HexDigit",
        "BLOCK_COMMENT",
        "LINE_COMMENT",
        "PYTHON_COMMENT",
        "WS",
    ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache()
        )
        self._actions = None
        self._predicates = None
