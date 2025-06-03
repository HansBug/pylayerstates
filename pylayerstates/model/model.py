import weakref
from typing import Optional, List, Dict, Tuple

from ..dsl import Program, parse_program, TransitionStatement, StateDefinition, EntryStatement


class Transition:
    def __init__(self, state: 'State', to_state_name: str, events: List[str], backward_layers: int = 0):
        self._state_ref = weakref.ref(state)
        self._to_state_name: str = to_state_name
        self._backward_layers: int = backward_layers
        self._events: List[str] = events

    @property
    def state(self) -> 'State':
        return self._state_ref()

    @property
    def model(self) -> 'Model':
        return self.state.model

    @property
    def to_state_name(self) -> str:
        return self._to_state_name

    @property
    def from_state(self) -> 'State':
        return self._state_ref()

    @property
    def to_state(self) -> 'State':
        return self.model.get_state(self._to_state_name)

    @property
    def events(self) -> List[str]:
        return self._events

    @property
    def backward_layers(self) -> int:
        return self._backward_layers

    @backward_layers.setter
    def backward_layers(self, new_layers: int):
        self._backward_layers = new_layers

    def rename_state(self, src_name: str, dst_name: str):
        if self._to_state_name == src_name:
            self._to_state_name = dst_name

    def to_node(self) -> TransitionStatement:
        return TransitionStatement(
            from_symbol=self.from_state.name,
            to_symbol=self._to_state_name,
            events=self._events,
            backward_layers=self.backward_layers if self.backward_layers != 0 else None,
        )


class State:
    def __init__(self, model: 'Model', name: str, display_name: Optional[str] = None,
                 substate_names: Optional[List[str]] = None, entry_state_name: Optional[str] = None,
                 transitions: Optional[List['Transition']] = None):
        self._model_ref = weakref.ref(model)
        self._name = name
        self._display_name = display_name if display_name is not None else self._name
        self._substates_names = list(substate_names or [])
        self._entry_state_name = entry_state_name
        self._transitions = list(transitions or [])

    @property
    def model(self) -> 'Model':
        return self._model_ref()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name):
        if self._name != new_name:
            self.model.rename_state(self._name, new_name)

    @property
    def display_name(self) -> str:
        return self._display_name

    @display_name.setter
    def display_name(self, new_display_name):
        self._display_name = new_display_name

    @property
    def substate_names(self) -> List[str]:
        return self._substates_names

    @property
    def substates(self) -> List['State']:
        return [
            self.model.get_state(name)
            for name in self._substates_names
        ]

    @property
    def entry_state_name(self) -> Optional[str]:
        return self._entry_state_name

    @entry_state_name.setter
    def entry_state_name(self, new_name: Optional[str]):
        self._entry_state_name = new_name

    @property
    def entry_state(self) -> Optional['State']:
        if self._entry_state_name is not None:
            return self.model.get_state(self.entry_state_name)
        else:
            return None

    @property
    def transitions(self) -> List['Transition']:
        return self._transitions

    @property
    def is_leaf(self):
        return bool(not self._substates_names and not self._entry_state_name)

    @is_leaf.setter
    def is_leaf(self, new_is_leaf):
        if self.is_leaf == bool(new_is_leaf):
            return
        if self.is_leaf and not new_is_leaf:
            raise RuntimeError(f'You cannot assign state {self!r} as non-leaf directly, '
                               f'just add its substates and entry, and it will become a non-leaf node.')
        if not self.is_leaf and new_is_leaf:
            self._substates_names.clear()
            self._entry_state_name = None

    def rename_state(self, src_name: str, dst_name: str):
        if self._name == src_name:
            self._name = dst_name
        for i in range(len(self._substates_names)):
            if self._substates_names[i] == src_name:
                self._substates_names[i] = dst_name
        if self._entry_state_name == src_name:
            self._entry_state_name = dst_name
        for trans in self._transitions:
            trans.rename_state(src_name, dst_name)

    def add_transition(self, to_state_name: str, events: List[str], backward_layers: int = 0) -> 'Transition':
        transition = Transition(
            state=self,
            to_state_name=to_state_name,
            events=events,
            backward_layers=backward_layers,
        )
        self._transitions.append(transition)
        return transition

    def to_node(self) -> StateDefinition:
        statements = []
        if self._entry_state_name is not None:
            statements.append(EntryStatement(self._entry_state_name))
        for state in self.substates:
            statements.append(state.to_node())
        for trans in self.transitions:
            statements.append(trans.to_node())

        return StateDefinition(
            name=self._name,
            display_name=None if self.display_name == self.name else self.display_name,
            statements=statements
        )


class Model:
    def __init__(self, states: Dict[str, State], root_state_name: str):
        self._states: Dict[str, State] = states
        self._root_state_name: str = root_state_name

    @property
    def root_state(self) -> State:
        return self.get_state(self._root_state_name)

    def get_state(self, name: str) -> State:
        return self._states[name]

    def add_state(self, name: str, display_name: Optional[str] = None, ):
        if name in self._states:
            raise ValueError(f'Duplicated model name - {name!r}')

        state = State(model=self, name=name, display_name=display_name)
        self._states[name] = state
        return state

    def rename_state(self, src_name: str, dst_name: str):
        if src_name in self._states:
            self._states[dst_name] = self._states[src_name]
            del self._states[src_name]
            for _, state in self._states.items():
                state.rename_state(src_name, dst_name)
        else:
            raise ValueError(f'State {src_name!r} not exist in model {self!r}.')
        return self

    @classmethod
    def from_program_node(cls, program: Program) -> 'Model':
        root_state_node = program.root_state
        all_transitions: List[Tuple[str, str, List[str], int]] = []
        model = Model({}, root_state_node.name)

        def _build_states(state_def: StateDefinition):
            state = model.add_state(name=state_def.name, display_name=state_def.display_name)
            for stats in state_def.statements:
                if isinstance(stats, EntryStatement):
                    if state.entry_state_name is not None:
                        raise ValueError(f'Duplicate entry state for state {state!r} - {stats.entry!r}.')
                    state.entry_state_name = stats.entry
                elif isinstance(stats, StateDefinition):
                    substate = _build_states(stats)
                    state.substate_names.append(substate.name)
                elif isinstance(stats, TransitionStatement):
                    all_transitions.append((
                        stats.from_symbol,
                        stats.to_symbol,
                        stats.events,
                        stats.backward_layers,
                    ))

            return state

        _build_states(root_state_node)

        for from_state_name, to_state_name, events, backward_layers in all_transitions:
            state = model.get_state(from_state_name)
            state.add_transition(
                to_state_name=to_state_name,
                events=events,
                backward_layers=backward_layers,
            )

        return model

    @classmethod
    def from_code(cls, code: str) -> 'Model':
        return cls.from_program_node(parse_program(code))

    def to_node(self):
        return Program(root_state=self.root_state.to_node())
