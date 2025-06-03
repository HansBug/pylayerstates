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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\3\3\5\3\33\n")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3)\n\3\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\5\7\5\64\n")
        buf.write("\5\f\5\16\5\67\13\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6?\n\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\5\7G\n\7\3\7\3\7\3\b\3\b\3\b\7")
        buf.write("\bN\n\b\f\b\16\bQ\13\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2Z\2\24\3\2\2\2\4(\3")
        buf.write("\2\2\2\6.\3\2\2\2\b\65\3\2\2\2\n>\3\2\2\2\f@\3\2\2\2\16")
        buf.write("J\3\2\2\2\20R\3\2\2\2\22T\3\2\2\2\24\25\5\4\3\2\25\26")
        buf.write("\7\2\2\3\26\3\3\2\2\2\27\30\7\3\2\2\30\32\7\20\2\2\31")
        buf.write("\33\5\6\4\2\32\31\3\2\2\2\32\33\3\2\2\2\33\34\3\2\2\2")
        buf.write("\34\35\7\n\2\2\35\36\5\b\5\2\36\37\7\13\2\2\37)\3\2\2")
        buf.write('\2 "\7\20\2\2!#\5\6\4\2"!\3\2\2\2"#\3\2\2\2#$\3\2\2')
        buf.write("\2$%\7\n\2\2%&\5\b\5\2&'\7\13\2\2')\3\2\2\2(\27\3\2")
        buf.write("\2\2( \3\2\2\2)\5\3\2\2\2*+\7\4\2\2+/\7\22\2\2,-\7\5\2")
        buf.write("\2-/\7\22\2\2.*\3\2\2\2.,\3\2\2\2/\7\3\2\2\2\60\64\5\n")
        buf.write("\6\2\61\64\5\4\3\2\62\64\5\f\7\2\63\60\3\2\2\2\63\61\3")
        buf.write("\2\2\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66")
        buf.write("\3\2\2\2\66\t\3\2\2\2\67\65\3\2\2\289\7\6\2\29:\7\20\2")
        buf.write("\2:?\7\17\2\2;<\7\7\2\2<=\7\20\2\2=?\7\17\2\2>8\3\2\2")
        buf.write("\2>;\3\2\2\2?\13\3\2\2\2@A\7\20\2\2AB\7\7\2\2BC\7\20\2")
        buf.write("\2CD\7\16\2\2DF\5\16\b\2EG\5\22\n\2FE\3\2\2\2FG\3\2\2")
        buf.write("\2GH\3\2\2\2HI\7\17\2\2I\r\3\2\2\2JO\5\20\t\2KL\7\b\2")
        buf.write("\2LN\5\20\t\2MK\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2")
        buf.write("P\17\3\2\2\2QO\3\2\2\2RS\7\20\2\2S\21\3\2\2\2TU\7\f\2")
        buf.write('\2UV\7\t\2\2VW\7\21\2\2WX\7\r\2\2X\23\3\2\2\2\13\32"')
        buf.write("(.\63\65>FO")
        return buf.getvalue()


class GrammarParser(Parser):
    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

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

    RULE_program = 0
    RULE_stateDefinition = 1
    RULE_namedAs = 2
    RULE_stateBody = 3
    RULE_entryStatement = 4
    RULE_transitionStatement = 5
    RULE_eventList = 6
    RULE_event = 7
    RULE_backwardDef = 8

    ruleNames = [
        "program",
        "stateDefinition",
        "namedAs",
        "stateBody",
        "entryStatement",
        "transitionStatement",
        "eventList",
        "event",
        "backwardDef",
    ]

    EOF = Token.EOF
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
            self.state = 18
            self.stateDefinition()
            self.state = 19
            self.match(GrammarParser.EOF)
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

        def STATE(self):
            return self.getToken(GrammarParser.STATE, 0)

        def LBRACE(self):
            return self.getToken(GrammarParser.LBRACE, 0)

        def stateBody(self):
            return self.getTypedRuleContext(GrammarParser.StateBodyContext, 0)

        def RBRACE(self):
            return self.getToken(GrammarParser.RBRACE, 0)

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def namedAs(self):
            return self.getTypedRuleContext(GrammarParser.NamedAsContext, 0)

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
        self.enterRule(localctx, 2, self.RULE_stateDefinition)
        self._la = 0  # Token type
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.STATE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(GrammarParser.STATE)
                self.state = 22
                localctx.symbol = self.match(GrammarParser.IDENTIFIER)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GrammarParser.NAMED or _la == GrammarParser.AS:
                    self.state = 23
                    self.namedAs()

                self.state = 26
                self.match(GrammarParser.LBRACE)
                self.state = 27
                self.stateBody()
                self.state = 28
                self.match(GrammarParser.RBRACE)
                pass
            elif token in [GrammarParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(GrammarParser.IDENTIFIER)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GrammarParser.NAMED or _la == GrammarParser.AS:
                    self.state = 31
                    self.namedAs()

                self.state = 34
                self.match(GrammarParser.LBRACE)
                self.state = 35
                self.stateBody()
                self.state = 36
                self.match(GrammarParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

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

        def NAMED(self):
            return self.getToken(GrammarParser.NAMED, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def AS(self):
            return self.getToken(GrammarParser.AS, 0)

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
        self.enterRule(localctx, 4, self.RULE_namedAs)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.NAMED]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(GrammarParser.NAMED)
                self.state = 41
                self.match(GrammarParser.STRING)
                pass
            elif token in [GrammarParser.AS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(GrammarParser.AS)
                self.state = 43
                self.match(GrammarParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

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

        def entryStatement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.EntryStatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.EntryStatementContext, i)

        def stateDefinition(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StateDefinitionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StateDefinitionContext, i)

        def transitionStatement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(
                    GrammarParser.TransitionStatementContext
                )
            else:
                return self.getTypedRuleContext(
                    GrammarParser.TransitionStatementContext, i
                )

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
        self.enterRule(localctx, 6, self.RULE_stateBody)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3F) == 0 and (
                (1 << _la)
                & (
                    (1 << GrammarParser.STATE)
                    | (1 << GrammarParser.ENTRY)
                    | (1 << GrammarParser.ARROW)
                    | (1 << GrammarParser.IDENTIFIER)
                )
            ) != 0:
                self.state = 49
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 4, self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.entryStatement()
                    pass

                elif la_ == 2:
                    self.state = 47
                    self.stateDefinition()
                    pass

                elif la_ == 3:
                    self.state = 48
                    self.transitionStatement()
                    pass

                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntryStatementContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.symbol = None  # Token

        def ENTRY(self):
            return self.getToken(GrammarParser.ENTRY, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def ARROW(self):
            return self.getToken(GrammarParser.ARROW, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_entryStatement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEntryStatement"):
                listener.enterEntryStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEntryStatement"):
                listener.exitEntryStatement(self)

    def entryStatement(self):
        localctx = GrammarParser.EntryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_entryStatement)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.ENTRY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(GrammarParser.ENTRY)
                self.state = 55
                localctx.symbol = self.match(GrammarParser.IDENTIFIER)
                self.state = 56
                self.match(GrammarParser.SEMICOLON)
                pass
            elif token in [GrammarParser.ARROW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(GrammarParser.ARROW)
                self.state = 58
                localctx.symbol = self.match(GrammarParser.IDENTIFIER)
                self.state = 59
                self.match(GrammarParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 10, self.RULE_transitionStatement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            localctx.fromSymbol = self.match(GrammarParser.IDENTIFIER)
            self.state = 63
            self.match(GrammarParser.ARROW)
            self.state = 64
            localctx.toSymbol = self.match(GrammarParser.IDENTIFIER)
            self.state = 65
            self.match(GrammarParser.COLON)
            self.state = 66
            self.eventList()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == GrammarParser.LPAREN:
                self.state = 67
                self.backwardDef()

            self.state = 70
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
        self.enterRule(localctx, 12, self.RULE_eventList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.event()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == GrammarParser.PLUS:
                self.state = 73
                self.match(GrammarParser.PLUS)
                self.state = 74
                self.event()
                self.state = 79
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
        self.enterRule(localctx, 14, self.RULE_event)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
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
        self.enterRule(localctx, 16, self.RULE_backwardDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(GrammarParser.LPAREN)
            self.state = 83
            self.match(GrammarParser.CARET)
            self.state = 84
            self.match(GrammarParser.INTEGER)
            self.state = 85
            self.match(GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
