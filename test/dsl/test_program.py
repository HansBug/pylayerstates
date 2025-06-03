import pytest

from pylayerstates.dsl import parse_program, GrammarParseError, SyntaxFailError
from pylayerstates.dsl.node import *


@pytest.mark.unittest
class TestDSLProgram:
    @pytest.mark.parametrize(['input_text', 'expected'], [
        ('state Z;', Program(root_state=StateDefinition(name='Z', display_name=None, is_entry=False, statements=[]))),
        ('Z;', Program(root_state=StateDefinition(name='Z', display_name=None, is_entry=False, statements=[]))),
        ("state Z as 'Zeta';",
         Program(root_state=StateDefinition(name='Z', display_name='Zeta', is_entry=False, statements=[]))),
        ("Z as 'Zeta';",
         Program(root_state=StateDefinition(name='Z', display_name='Zeta', is_entry=False, statements=[]))),
        ('state Z {}', Program(root_state=StateDefinition(name='Z', display_name=None, is_entry=False, statements=[]))),
        ("Z as 'Zeta' {}",
         Program(root_state=StateDefinition(name='Z', display_name='Zeta', is_entry=False, statements=[]))),
        ('entry state Z {}',
         Program(root_state=StateDefinition(name='Z', display_name=None, is_entry=True, statements=[]))),
        ("-> Z as 'Zeta';",
         Program(root_state=StateDefinition(name='Z', display_name='Zeta', is_entry=True, statements=[]))),
        (
                '\n# fuck yourself\n/* state Z; \nstate ZZ {\n}\n*/\nstate X {\n    -> Y;\n\n    // nihao\n    state Z as "看目前是怎么个设计+" {\n        -> state Z1 {\n            -> Z2 : E1;\n        }\n        Z2;\n        Z3;\n        Z4;\n        \n        Z2 -> Z3 : E1 + E2;\n        Z3 -> Z4 : E4 (^2);\n    }\n\n    TT {\n    };;;;\n}\n    ',
                Program(root_state=StateDefinition(name='X', display_name=None, is_entry=False, statements=[
                    StateDefinition(name='Y', display_name=None, is_entry=True, statements=[]),
                    StateDefinition(name='Z', display_name='看目前是怎么个设计+', is_entry=False, statements=[
                        StateDefinition(name='Z1', display_name=None, is_entry=True, statements=[
                            TransitionStatement(from_symbol=None, to_symbol='Z2', events=['E1'],
                                                backward_layers=None)]),
                        StateDefinition(name='Z2', display_name=None, is_entry=False, statements=[]),
                        StateDefinition(name='Z3', display_name=None, is_entry=False, statements=[]),
                        StateDefinition(name='Z4', display_name=None, is_entry=False, statements=[]),
                        TransitionStatement(from_symbol='Z2', to_symbol='Z3', events=['E1', 'E2'],
                                            backward_layers=None),
                        TransitionStatement(from_symbol='Z3', to_symbol='Z4', events=['E4'], backward_layers=2)]),
                    StateDefinition(name='TT', display_name=None, is_entry=False, statements=[])]))),
    ])
    def test_positive_cases(self, input_text, expected):
        assert parse_program(input_text) == expected

    @pytest.mark.parametrize(['input_text', 'expected_str'], [
        ('state Z;', 'Z;\n'),
        ('Z;', 'Z;\n'),
        ("state Z as 'Zeta';", "Z as 'Zeta';\n"),
        ("Z as 'Zeta';", "Z as 'Zeta';\n"),
        ('state Z {}', 'Z;\n'),
        ("Z as 'Zeta' {}", "Z as 'Zeta';\n"),
        ('entry state Z {}', '-> Z;\n'),
        ("-> Z as 'Zeta';", "-> Z as 'Zeta';\n"),
        (
                '\n# fuck yourself\n/* state Z; \nstate ZZ {\n}\n*/\nstate X {\n    -> Y;\n\n    // nihao\n    state Z as "看目前是怎么个设计+" {\n        -> state Z1 {\n            -> Z2 : E1;\n        }\n        Z2;\n        Z3;\n        Z4;\n        \n        Z2 -> Z3 : E1 + E2;\n        Z3 -> Z4 : E4 (^2);\n    }\n\n    TT {\n    };;;;\n}\n    ',
                "X {\n    -> Y;\n    Z as '看目前是怎么个设计+' {\n        -> Z1 {\n            -> Z2 : E1;\n        }\n        Z2;\n        Z3;\n        Z4;\n        Z2 -> Z3 : E1 + E2;\n        Z3 -> Z4 : E4 (^2);\n    }\n    TT;\n}\n"),
    ])
    def test_positive_cases_str(self, input_text, expected_str, text_aligner):
        text_aligner.assert_equal(
            expected_str,
            str(parse_program(input_text)),
        )

    @pytest.mark.parametrize(['input_text'], [
        ("state;",),
        ("state 999;",),
        ("-> X",),
        ("999;",),
        ("state as \'XXX\';",),
        ("state X",),
        ("X",),
    ])
    def test_negative_cases(self, input_text):
        with pytest.raises(GrammarParseError) as ei:
            parse_program(input_text)

        err = ei.value
        assert isinstance(err, GrammarParseError)
        assert len(err.errors) > 0
        assert len([e for e in err.errors if isinstance(e, SyntaxFailError)]) > 0
        assert f'Found {len(err.errors)} errors during parsing:' in err.args[0]
