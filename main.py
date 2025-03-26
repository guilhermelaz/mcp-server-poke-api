from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx

load_dotenv()

mcp = FastMCP("API_POKEMON")

USER_AGENT = "API_POKEMON"

#https://pokeapi.co/api/v2/pokemon/
@mcp.tool()
async def search_pokemon(name: str) -> dict | None:
    """
    Search for a pokemon by name

    Args:
        name (str): The name of the pokemon

    Returns:
        List of pokemon data
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error: {e}")
        return None


#https://pokeapi.co/api/v2/ability/
@mcp.tool()
async def get_pokemon_abilities(name: str) -> dict | None:
    """
    Get the abilities of a pokemon

    Args:
        name (str): The name of the pokemon

    Returns:
        List of pokemon abilities data
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"https://pokeapi.co/api/v2/ability/{name}")
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error: {e}")
        return None


if __name__ == "__main__":
    import os
    # Use environment variables with defaults for configuration
    host = os.getenv("MCP_HOST", "0.0.0.0")
    port = int(os.getenv("MCP_PORT", "8000"))
    
    # Use HTTP transport for server deployment
    mcp.run(transport="http")
