import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="a = [1]; del a[0]",
    working_directory="dummy_linea_repo/",
    session_name=None,
    user_name=None,
    hardware_spec=None,
    libraries=[],
)
literal_1 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=5,
    end_lineno=1,
    end_col_offset=6,
    value=1,
)
lookup_1 = LookupNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    name="__build_list__",
    value=None,
)
lookup_2 = LookupNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    name="delitem",
    value=None,
)
literal_2 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=15,
    end_lineno=1,
    end_col_offset=16,
    value=0,
)
argument_1 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=literal_1.id,
    value_literal=None,
)
argument_2 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=1,
    value_node_id=literal_2.id,
    value_literal=None,
)
call_1 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=0,
    end_lineno=1,
    end_col_offset=7,
    arguments=[argument_1.id],
    function_id=lookup_1.id,
    value=None,
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    source_node_id=call_1.id,
    assigned_variable_name="a",
    value=None,
)
argument_3 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=variable_1.id,
    value_literal=None,
)
call_2 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=9,
    end_lineno=1,
    end_col_offset=17,
    arguments=[argument_2.id, argument_3.id],
    function_id=lookup_2.id,
    value=None,
)
