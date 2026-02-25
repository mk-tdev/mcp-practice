from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-first-mcp-server with stdio transport")

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")
