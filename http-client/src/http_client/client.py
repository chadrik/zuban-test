import httpx
from typing import Dict, Any, cast


def fetch_data(url: str) -> Dict[str, Any]:
    """Fetch data from a URL using httpx."""
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
        return cast(Dict[str, Any], response.json())


async def fetch_data_async(url: str) -> Dict[str, Any]:
    """Fetch data from a URL using httpx asynchronously."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return cast(Dict[str, Any], response.json())