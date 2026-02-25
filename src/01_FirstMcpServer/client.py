import asyncio
from mcp.client.streamable_http import streamable_http_client
from mcp import ClientSession

async def main():
    async with streamable_http_client("http://127.0.0.1:8000/mcp") as (read, write, get_session_id):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # print session ID
            print("Session ID:", get_session_id())
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

if __name__ == "__main__":
    asyncio.run(main())
