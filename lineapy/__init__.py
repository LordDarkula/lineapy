from lineapy.constants import ExecutionMode
from lineapy.data.graph import Graph
from lineapy.data.types import SessionType
from lineapy.instrumentation.tracer import Tracer
from lineapy.instrumentation.variable import Variable
from lineapy.utils import FunctionShouldNotBeCalled

__version__ = "0.0.1"

from typing import Any, Optional


def linea_publish(variable: Any, description: Optional[str] = None) -> None:
    """
    Publishes artifact to the linea repo
    """
    """
    DEV NOTEs:
    - This method is instrumented by transformer to be called by the tracer
    """

    raise FunctionShouldNotBeCalled(
        """This method must be used along with a custom Linea Kernel,
          or the Linea Cli."""
    )


__all__ = [
    "Graph",
    "Tracer",
    "Variable",
    "linea_publish",
    "SessionType",
    "ExecutionMode",
    "__version__",
]
