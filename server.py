from typing import Annotated

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field


mcp = FastMCP("Smart_home", stateless_http=True, json_response=True)


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def Smart_home(
    nowy_kolor: Annotated[
        str,
        Field(
            min_length=7,
            max_length=7,
            pattern=r"^#[0-9A-Fa-f]{6}$",
            description="Kolor RGB w formacie #RRGGBB, np. #FFAABB.",
        ),
    ],
) -> dict[str, str]:
    """Sprawdza kolor HEX i zwraca przyjętą wartość wielkimi literami."""
    return {"nowy_kolor": nowy_kolor.upper()}


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
