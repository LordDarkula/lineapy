import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.STATIC,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="def foo(a, b):\n    return a - b\nc = foo(b=1, a=2)\n",
    working_directory="dummy_linea_repo/",
    libraries=[],
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=3,
        col_offset=0,
        end_lineno=3,
        end_col_offset=17,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                keyword="a",
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=3,
                    col_offset=15,
                    end_lineno=3,
                    end_col_offset=16,
                    value=2,
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                keyword="b",
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=3,
                    col_offset=10,
                    end_lineno=3,
                    end_col_offset=11,
                    value=1,
                ).id,
            ).id,
        ],
        function_id=FunctionDefinitionNode(
            id=get_new_id(),
            session_id=session.id,
            lineno=1,
            col_offset=0,
            end_lineno=2,
            end_col_offset=16,
            output_state_change_nodes=[],
            input_state_change_nodes=[],
            import_nodes=[],
            function_name="foo",
        ).id,
    ).id,
    assigned_variable_name="c",
)