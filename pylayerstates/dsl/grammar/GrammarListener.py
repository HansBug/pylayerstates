# Generated from ./pylayerstates/dsl/grammar/Grammar.g4 by ANTLR 4.9.3
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser


# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):
    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx: GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx: GrammarParser.ProgramContext):
        pass

    # Enter a parse tree produced by GrammarParser#stateDefinition.
    def enterStateDefinition(self, ctx: GrammarParser.StateDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#stateDefinition.
    def exitStateDefinition(self, ctx: GrammarParser.StateDefinitionContext):
        pass

    # Enter a parse tree produced by GrammarParser#namedAs.
    def enterNamedAs(self, ctx: GrammarParser.NamedAsContext):
        pass

    # Exit a parse tree produced by GrammarParser#namedAs.
    def exitNamedAs(self, ctx: GrammarParser.NamedAsContext):
        pass

    # Enter a parse tree produced by GrammarParser#stateBody.
    def enterStateBody(self, ctx: GrammarParser.StateBodyContext):
        pass

    # Exit a parse tree produced by GrammarParser#stateBody.
    def exitStateBody(self, ctx: GrammarParser.StateBodyContext):
        pass

    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx: GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx: GrammarParser.StatementContext):
        pass

    # Enter a parse tree produced by GrammarParser#entryStatement.
    def enterEntryStatement(self, ctx: GrammarParser.EntryStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#entryStatement.
    def exitEntryStatement(self, ctx: GrammarParser.EntryStatementContext):
        pass

    # Enter a parse tree produced by GrammarParser#transitionStatement.
    def enterTransitionStatement(self, ctx: GrammarParser.TransitionStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#transitionStatement.
    def exitTransitionStatement(self, ctx: GrammarParser.TransitionStatementContext):
        pass

    # Enter a parse tree produced by GrammarParser#eventList.
    def enterEventList(self, ctx: GrammarParser.EventListContext):
        pass

    # Exit a parse tree produced by GrammarParser#eventList.
    def exitEventList(self, ctx: GrammarParser.EventListContext):
        pass

    # Enter a parse tree produced by GrammarParser#event.
    def enterEvent(self, ctx: GrammarParser.EventContext):
        pass

    # Exit a parse tree produced by GrammarParser#event.
    def exitEvent(self, ctx: GrammarParser.EventContext):
        pass

    # Enter a parse tree produced by GrammarParser#backwardDef.
    def enterBackwardDef(self, ctx: GrammarParser.BackwardDefContext):
        pass

    # Exit a parse tree produced by GrammarParser#backwardDef.
    def exitBackwardDef(self, ctx: GrammarParser.BackwardDefContext):
        pass


del GrammarParser
