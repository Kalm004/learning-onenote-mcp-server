from fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

load_dotenv()

ONENOTE_TOKEN = os.getenv("ONENOTE_TOKEN")

mcp = FastMCP("OneNote MCP Server")

# Example tool
@mcp.tool(
    name="getNotes",
    description="This tool provides access to the user's OneNote notes."
)
def getNotes() -> dict:
    return getNotesFromOneNote()

@mcp.tool(
    name="getNoteContent",
    description="This tool fetches the content of a specific OneNote page by its contentUrl."
)
def getNoteContent(contentUrl: str) -> dict:
    return getNoteContentFromOneNote(contentUrl)

def getNotesFromOneNote() -> dict:
    response = requests.get("https://graph.microsoft.com/v1.0/me/onenote/pages", headers={"Authorization": f"Bearer {ONENOTE_TOKEN}"})
    if response.status_code == 200:
        # Return only title and contentUrl and parentSection.displayName
        notes = []
        for note in response.json()["value"]:
            notes.append({
                "title": note["title"],
                "contentUrl": note["contentUrl"],
                "parentSection": note["parentSection"]["displayName"]
            })
        return {
            "notes": notes
        }
    else:
        return {
            "error": "Failed to get notes from OneNote"
        }

def getNoteContentFromOneNote(contentUrl: str) -> dict:
    response = requests.get(contentUrl, headers={"Authorization": f"Bearer {ONENOTE_TOKEN}"})
    if response.status_code == 200:
        return {
            "content": response.text,
            "contentType": response.headers.get("Content-Type", "text/html")
        }
    else:
        return {
            "error": f"Failed to get note content. Status code: {response.status_code}"
        }

if __name__ == "__main__":
    mcp.run()