# Learning - MCP Server - OneNote

## MCP

MCP is a protocol for providing tools, prompts and resources for LLMs.  

In this protocol, there are servers and clients. 

Servers provide: 

- Tools 
- Prompts 
- Resources 

Clients provide: 

- Sampling 
- Roots 
- Elicitation 

[MCP Documentation](https://modelcontextprotocol.io/docs/learn/architecture)

MCP uses JSON-RPC.

Client-host-server architecture. Host is the one that manages the clients and the context, each client connects to a single server.

## About this project

The goal of this project is documenting my own knowledge on MCP by creating a simple implementation of a MCP Server for OneNote.

**Disclaimer:** This isn't meant to be a comprehensive implementation of a MCP server for OneNote.

### Usage

For adding this MCP Server to Cursor, edit your `~/.cursor/mcp.json` and add the following:

``` JSON
    "onenote": {
      "command": "<venv-path>/python.exe",
      "args": ["<this-project-path>/src/server.py"],
      "description": "This MCP server provides access to the user's OneNote notes."
    }
```