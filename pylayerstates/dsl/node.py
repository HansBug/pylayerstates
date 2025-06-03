import io
from abc import ABC
from dataclasses import dataclass
from textwrap import indent
from typing import List, Optional, Union

__all__ = [
    'ASTNode',
    'Program',
    'TransitionStatement',
    'StateDefinition',
]


@dataclass
class ASTNode(ABC):
    def __str__(self):
        with io.StringIO() as sf:
            self._print_to_str(sf)
            return sf.getvalue()

    def _print_to_str(self, sf):
        raise NotImplementedError  # pragma: no cover


@dataclass
class Program(ASTNode):
    root_state: 'StateDefinition'

    def _print_to_str(self, sf):
        self.root_state._print_to_str(sf)


@dataclass
class TransitionStatement(ASTNode):
    from_symbol: Optional[str]
    to_symbol: str
    events: List[str]
    backward_layers: Optional[int] = None

    def _print_to_str(self, sf):
        if self.from_symbol is not None:
            print(f'{self.from_symbol} -> {self.to_symbol} : {" + ".join(self.events)}', file=sf, end='')
        else:
            print(f'-> {self.to_symbol} : {" + ".join(self.events)}', file=sf, end='')
        if self.backward_layers is not None:
            print(f' (^{self.backward_layers})', file=sf, end='')
        print(f';', file=sf)


@dataclass
class StateDefinition(ASTNode):
    name: str
    display_name: Optional[str]
    is_entry: bool
    statements: List[Union['TransitionStatement', 'StateDefinition']]

    def _print_to_str(self, sf):
        if self.display_name is not None:
            print(f'{"-> " if self.is_entry else ""}{self.name} as {self.display_name!r}', file=sf, end='')
        else:
            print(f'{"-> " if self.is_entry else ""}{self.name}', file=sf, end='')

        if self.statements:
            print(' {', file=sf)
            for i, stat in enumerate(self.statements):
                print(indent(str(stat), prefix='    ').rstrip(), file=sf)
            print('}', file=sf)
        else:
            print(';', file=sf)
