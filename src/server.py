from fastmcp import FastMCP

mcp = FastMCP("OneNote MCP Server")

# Example tool
@mcp.tool(
    name="getNotes",
    description="This tool provides access to the user's OneNote notes."
)
def getNotes() -> dict:
    return {
        "notes": [
            {
                "title": "Note 1",
                "content": "Content 1"
            },
        ]
    }

if __name__ == "__main__":
    mcp.run()