import asyncio
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
import sys
from pathlib import Path

async def main():
  server_path = Path(__file__).resolve().with_name("server.py")
  server_params = StdioServerParameters(
    command=sys.executable,
    args=[str(server_path)],
    env=None,
  )
  
  async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
      await session.initialize()
      print("Initialized MCP session")
      tools = await session.list_tools()
      print("-" * 50)
      print("Available tools:", tools)
      print("-" * 50)
      
      print("-" * 50)
      # call tool
      result = await session.call_tool("hello", {"name": "World"})
      print("Tool result:", result)
      print("-" * 50)
      
      # call another tool
      result = await session.call_tool("add", {"a": 1, "b": 2})
      print("Tool result:", result)
      print("-" * 50)

if __name__ == "__main__":
    asyncio.run(main())
