from .grammar import GrammarListener, GrammarParser
from .node import TransitionStatement, StateDefinition, Program


class GrammarParseListener(GrammarListener):
    def __init__(self):
        super().__init__()
        self.nodes = {}

    def exitProgram(self, ctx: GrammarParser.ProgramContext):
        super().exitProgram(ctx)
        self.nodes[ctx] = Program(
            init_state=self.nodes[ctx.entryDefinition()],
            root_state=self.nodes[ctx.stateDefinition()],
        )

    def exitEntryDefinition(self, ctx: GrammarParser.EntryDefinitionContext):
        super().exitEntryDefinition(ctx)
        self.nodes[ctx] = ctx.symbol.text

    def exitStateDefinition(self, ctx: GrammarParser.StateDefinitionContext):
        super().exitStateDefinition(ctx)
        self.nodes[ctx] = StateDefinition(
            name=ctx.symbol.text,
            display_name=self.nodes[ctx.namedAs()] if ctx.namedAs() is not None else None,
            statements=self.nodes[ctx.stateBody()] if ctx.stateBody() is not None else [],
        )

    def exitNamedAs(self, ctx: GrammarParser.NamedAsContext):
        super().exitNamedAs(ctx)
        self.nodes[ctx] = eval(ctx.STRING().getText())

    def exitStateBody(self, ctx: GrammarParser.StateBodyContext):
        super().exitStateBody(ctx)
        self.nodes[ctx] = [
            self.nodes[stat] for stat in ctx.statement()
            if stat in self.nodes
        ]

    def exitStatement(self, ctx: GrammarParser.StatementContext):
        super().exitStatement(ctx)
        node = ctx.transitionStatement() or ctx.stateDefinition()
        if node is not None:
            self.nodes[ctx] = self.nodes[node]

    def exitTransitionStatement(self, ctx: GrammarParser.TransitionStatementContext):
        super().exitTransitionStatement(ctx)
        self.nodes[ctx] = TransitionStatement(
            from_symbol=ctx.fromSymbol.text if ctx.fromSymbol is not None else None,
            to_symbol=ctx.toSymbol.text,
            events=self.nodes[ctx.eventList()],
            backward_layers=self.nodes[ctx.backwardDef()] if ctx.backwardDef() is not None else None,
        )

    def exitEventList(self, ctx: GrammarParser.EventListContext):
        super().exitEventList(ctx)
        event_names = []
        for event in ctx.event():
            event_names.append(self.nodes[event])
        self.nodes[ctx] = event_names

    def exitEvent(self, ctx: GrammarParser.EventContext):
        super().exitEvent(ctx)
        event_name = ctx.IDENTIFIER().getText()
        self.nodes[ctx] = event_name

    def exitBackwardDef(self, ctx: GrammarParser.BackwardDefContext):
        super().exitBackwardDef(ctx)
        layers = int(ctx.INTEGER().getText())
        self.nodes[ctx] = layers
