import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""import lineapy
a = 10
b = lambda x: x + 10
c = b(a)

lineapy.save(c, \'c\')
""",
    location=PosixPath("[source file path]"),
)
call_3 = CallNode(
    source_location=SourceLocation(
        lineno=4,
        col_offset=4,
        end_lineno=4,
        end_col_offset=8,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        function_id=LookupNode(
            name="getitem",
        ).id,
        positional_args=[
            CallNode(
                source_location=SourceLocation(
                    lineno=3,
                    col_offset=4,
                    end_lineno=3,
                    end_col_offset=20,
                    source_code=source_1.id,
                ),
                function_id=LookupNode(
                    name="__exec__",
                ).id,
                positional_args=[
                    LiteralNode(
                        value="lambda x: x + 10",
                    ).id,
                    LiteralNode(
                        value=True,
                    ).id,
                ],
            ).id,
            LiteralNode(
                value=0,
            ).id,
        ],
    ).id,
    positional_args=[
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=4,
                end_lineno=2,
                end_col_offset=6,
                source_code=source_1.id,
            ),
            value=10,
        ).id
    ],
)
