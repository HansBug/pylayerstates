# Generated from ./pylayerstates/dsl/grammar/Grammar.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write('\3\3\3\3\3\3\3\3\3\4\5\4"\n\4\3\4\3\4\5\4&\n\4\3\4\3')
        buf.write("\4\3\4\3\4\3\4\5\4-\n\4\3\4\3\4\5\4\61\n\4\3\4\5\4\64")
        buf.write("\n\4\3\5\3\5\3\6\3\6\3\6\3\7\7\7<\n\7\f\7\16\7?\13\7\3")
        buf.write("\b\3\b\3\b\5\bD\n\b\3\t\5\tG\n\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\tN\n\t\3\t\3\t\3\n\3\n\3\n\7\nU\n\n\f\n\16\nX\13\n\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\2\3\4\2\3\3\6\6\2`\2\30\3\2\2\2\4\34\3\2")
        buf.write("\2\2\6\63\3\2\2\2\b\65\3\2\2\2\n\67\3\2\2\2\f=\3\2\2\2")
        buf.write("\16C\3\2\2\2\20F\3\2\2\2\22Q\3\2\2\2\24Y\3\2\2\2\26[\3")
        buf.write("\2\2\2\30\31\5\4\3\2\31\32\5\6\4\2\32\33\7\2\2\3\33\3")
        buf.write("\3\2\2\2\34\35\5\b\5\2\35\36\7\17\2\2\36\37\7\16\2\2\37")
        buf.write('\5\3\2\2\2 "\7\4\2\2! \3\2\2\2!"\3\2\2\2"#\3\2\2\2')
        buf.write("#%\7\17\2\2$&\5\n\6\2%$\3\2\2\2%&\3\2\2\2&'\3\2\2\2'")
        buf.write("(\7\t\2\2()\5\f\7\2)*\7\n\2\2*\64\3\2\2\2+-\7\4\2\2,+")
        buf.write("\3\2\2\2,-\3\2\2\2-.\3\2\2\2.\60\7\17\2\2/\61\5\n\6\2")
        buf.write("\60/\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\64\7\16\2")
        buf.write("\2\63!\3\2\2\2\63,\3\2\2\2\64\7\3\2\2\2\65\66\t\2\2\2")
        buf.write("\66\t\3\2\2\2\678\7\5\2\289\7\21\2\29\13\3\2\2\2:<\5\16")
        buf.write("\b\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\r\3\2\2")
        buf.write("\2?=\3\2\2\2@D\5\6\4\2AD\5\20\t\2BD\7\16\2\2C@\3\2\2\2")
        buf.write("CA\3\2\2\2CB\3\2\2\2D\17\3\2\2\2EG\7\17\2\2FE\3\2\2\2")
        buf.write("FG\3\2\2\2GH\3\2\2\2HI\7\6\2\2IJ\7\17\2\2JK\7\r\2\2KM")
        buf.write("\5\22\n\2LN\5\26\f\2ML\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7")
        buf.write("\16\2\2P\21\3\2\2\2QV\5\24\13\2RS\7\7\2\2SU\5\24\13\2")
        buf.write("TR\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\23\3\2\2\2X")
        buf.write("V\3\2\2\2YZ\7\17\2\2Z\25\3\2\2\2[\\\7\13\2\2\\]\7\b\2")
        buf.write("\2]^\7\20\2\2^_\7\f\2\2_\27\3\2\2\2\f!%,\60\63=CFMV")
        return buf.getvalue()


class GrammarParser(Parser):
    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "'entry'",
        "'state'",
        "'as'",
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
        "<INVALID>",
        "STATE",
        "AS",
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

    RULE_program = 0
    RULE_entryDefinition = 1
    RULE_stateDefinition = 2
    RULE_entryMark = 3
    RULE_namedAs = 4
    RULE_stateBody = 5
    RULE_statement = 6
    RULE_transitionStatement = 7
    RULE_eventList = 8
    RULE_event = 9
    RULE_backwardDef = 10

    ruleNames = [
        "program",
        "entryDefinition",
        "stateDefinition",
        "entryMark",
        "namedAs",
        "stateBody",
        "statement",
        "transitionStatement",
        "eventList",
        "event",
        "backwardDef",
    ]

    EOF = Token.EOF
    T__0 = 1
    STATE = 2
    AS = 3
    ARROW = 4
    PLUS = 5
    CARET = 6
    LBRACE = 7
    RBRACE = 8
    LPAREN = 9
    RPAREN = 10
    COLON = 11
    SEMICOLON = 12
    IDENTIFIER = 13
    INTEGER = 14
    STRING = 15
    BLOCK_COMMENT = 16
    LINE_COMMENT = 17
    PYTHON_COMMENT = 18
    WS = 19

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class ProgramContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entryDefinition(self):
            return self.getTypedRuleContext(GrammarParser.EntryDefinitionContext, 0)

        def stateDefinition(self):
            return self.getTypedRuleContext(GrammarParser.StateDefinitionContext, 0)

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_program

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)

    def program(self):
        localctx = GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.entryDefinition()
            self.state = 23
            self.stateDefinition()
            self.state = 24
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntryDefinitionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.symbol = None  # Token

        def entryMark(self):
            return self.getTypedRuleContext(GrammarParser.EntryMarkContext, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_entryDefinition

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEntryDefinition"):
                listener.enterEntryDefinition(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEntryDefinition"):
                listener.exitEntryDefinition(self)

    def entryDefinition(self):
        localctx = GrammarParser.EntryDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entryDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.entryMark()
            self.state = 27
            localctx.symbol = self.match(GrammarParser.IDENTIFIER)
            self.state = 28
            self.match(GrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StateDefinitionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.symbol = None  # Token

        def LBRACE(self):
            return self.getToken(GrammarParser.LBRACE, 0)

        def stateBody(self):
            return self.getTypedRuleContext(GrammarParser.StateBodyContext, 0)

        def RBRACE(self):
            return self.getToken(GrammarParser.RBRACE, 0)

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def STATE(self):
            return self.getToken(GrammarParser.STATE, 0)

        def namedAs(self):
            return self.getTypedRuleContext(GrammarParser.NamedAsContext, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_stateDefinition

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStateDefinition"):
                listener.enterStateDefinition(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStateDefinition"):
                listener.exitStateDefinition(self)

    def stateDefinition(self):
        localctx = GrammarParser.StateDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stateDefinition)
        self._la = 0  # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 4, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GrammarParser.STATE:
                    self.state = 30
                    self.match(GrammarParser.STATE)

                self.state = 33
                localctx.symbol = self.match(GrammarParser.IDENTIFIER)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GrammarParser.AS:
                    self.state = 34
                    self.namedAs()

                self.state = 37
                self.match(GrammarParser.LBRACE)
                self.state = 38
                self.stateBody()
                self.state = 39
                self.match(GrammarParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GrammarParser.STATE:
                    self.state = 41
                    self.match(GrammarParser.STATE)

                self.state = 44
                localctx.symbol = self.match(GrammarParser.IDENTIFIER)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GrammarParser.AS:
                    self.state = 45
                    self.namedAs()

                self.state = 48
                self.match(GrammarParser.SEMICOLON)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntryMarkContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(GrammarParser.ARROW, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_entryMark

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEntryMark"):
                listener.enterEntryMark(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEntryMark"):
                listener.exitEntryMark(self)

    def entryMark(self):
        localctx = GrammarParser.EntryMarkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_entryMark)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not (_la == GrammarParser.T__0 or _la == GrammarParser.ARROW):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamedAsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AS(self):
            return self.getToken(GrammarParser.AS, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_namedAs

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNamedAs"):
                listener.enterNamedAs(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNamedAs"):
                listener.exitNamedAs(self)

    def namedAs(self):
        localctx = GrammarParser.NamedAsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_namedAs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(GrammarParser.AS)
            self.state = 54
            self.match(GrammarParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StateBodyContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_stateBody

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStateBody"):
                listener.enterStateBody(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStateBody"):
                listener.exitStateBody(self)

    def stateBody(self):
        localctx = GrammarParser.StateBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stateBody)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3F) == 0 and (
                (1 << _la)
                & (
                    (1 << GrammarParser.STATE)
                    | (1 << GrammarParser.ARROW)
                    | (1 << GrammarParser.SEMICOLON)
                    | (1 << GrammarParser.IDENTIFIER)
                )
            ) != 0:
                self.state = 56
                self.statement()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stateDefinition(self):
            return self.getTypedRuleContext(GrammarParser.StateDefinitionContext, 0)

        def transitionStatement(self):
            return self.getTypedRuleContext(GrammarParser.TransitionStatementContext, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement"):
                listener.enterStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement"):
                listener.exitStatement(self)

    def statement(self):
        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 6, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.stateDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.transitionStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(GrammarParser.SEMICOLON)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransitionStatementContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fromSymbol = None  # Token
            self.toSymbol = None  # Token

        def ARROW(self):
            return self.getToken(GrammarParser.ARROW, 0)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def eventList(self):
            return self.getTypedRuleContext(GrammarParser.EventListContext, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def IDENTIFIER(self, i: int = None):
            if i is None:
                return self.getTokens(GrammarParser.IDENTIFIER)
            else:
                return self.getToken(GrammarParser.IDENTIFIER, i)

        def backwardDef(self):
            return self.getTypedRuleContext(GrammarParser.BackwardDefContext, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_transitionStatement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTransitionStatement"):
                listener.enterTransitionStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTransitionStatement"):
                listener.exitTransitionStatement(self)

    def transitionStatement(self):
        localctx = GrammarParser.TransitionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_transitionStatement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == GrammarParser.IDENTIFIER:
                self.state = 67
                localctx.fromSymbol = self.match(GrammarParser.IDENTIFIER)

            self.state = 70
            self.match(GrammarParser.ARROW)
            self.state = 71
            localctx.toSymbol = self.match(GrammarParser.IDENTIFIER)
            self.state = 72
            self.match(GrammarParser.COLON)
            self.state = 73
            self.eventList()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == GrammarParser.LPAREN:
                self.state = 74
                self.backwardDef()

            self.state = 77
            self.match(GrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventListContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def event(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.EventContext)
            else:
                return self.getTypedRuleContext(GrammarParser.EventContext, i)

        def PLUS(self, i: int = None):
            if i is None:
                return self.getTokens(GrammarParser.PLUS)
            else:
                return self.getToken(GrammarParser.PLUS, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_eventList

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEventList"):
                listener.enterEventList(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEventList"):
                listener.exitEventList(self)

    def eventList(self):
        localctx = GrammarParser.EventListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_eventList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.event()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == GrammarParser.PLUS:
                self.state = 80
                self.match(GrammarParser.PLUS)
                self.state = 81
                self.event()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_event

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEvent"):
                listener.enterEvent(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEvent"):
                listener.exitEvent(self)

    def event(self):
        localctx = GrammarParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_event)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BackwardDefContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def CARET(self):
            return self.getToken(GrammarParser.CARET, 0)

        def INTEGER(self):
            return self.getToken(GrammarParser.INTEGER, 0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_backwardDef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBackwardDef"):
                listener.enterBackwardDef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBackwardDef"):
                listener.exitBackwardDef(self)

    def backwardDef(self):
        localctx = GrammarParser.BackwardDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_backwardDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(GrammarParser.LPAREN)
            self.state = 90
            self.match(GrammarParser.CARET)
            self.state = 91
            self.match(GrammarParser.INTEGER)
            self.state = 92
            self.match(GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
