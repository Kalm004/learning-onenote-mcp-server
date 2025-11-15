# Learning - MCP Server - OneNote

## About this project

The goal of this project is documenting my own knowledge on MCP by creating a simple implementation of a MCP Server for OneNote.

**Disclaimer:** This isn't meant to be a comprehensive implementation of a MCP server for OneNote.

This project uses Microsoft Graph Explorer to get OneNote information. You can get your access token here: [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer?request=me/onenote/notebooks&version=v1.0)

### Running this project

An `.env` file needs to be created inside the `.src` folder. The following environment variables need to be defined there:

| Name          | Description                                             |
|---------------|---------------------------------------------------------|
| ONENOTE_TOKEN | Graph Explorer token with permissions to read OneNote notes |

# TOON usage
This project uses TOON as the response format of the getNotes tool just as a way of testing TOON. For TOON encoding this project is using: [Toon-Python](https://github.com/toon-format/toon-python).

Using TOON I see a 30% reduction on the number of output tokens of MCP tool.

### Usage

For adding this MCP Server to Cursor, edit your `~/.cursor/mcp.json` and add the following:

``` JSON
    "onenote": {
      "command": "<venv-path>/python.exe",
      "args": ["<this-project-path>/src/server.py"],
      "description": "This MCP server provides access to the user's OneNote notes."
    }
```

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

