import asyncio
import httpx


class RickAndMortyClient:
    """
    Class-based client for the Rick and Morty API.
    """

    def __init__(self, base_url: str):
        self.base_url = base_url

    async def fetch_all_characters(self):
        url = f"{self.base_url}/character"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            results = data["results"]
            total_pages = data["info"]["pages"]

            tasks = [client.get(f"{url}?page={page}") for page in range(2, total_pages + 1)]
            responses = await asyncio.gather(*tasks)
            for resp in responses:
                resp.raise_for_status()
                results.extend(resp.json()["results"])
        return results


    async def fetch_all_locations(self):
        url = f"{self.base_url}/location"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            results = data["results"]
            total_pages = data["info"]["pages"]

            tasks = [client.get(f"{url}?page={p}") for p in range(2, total_pages + 1)]
            responses = await asyncio.gather(*tasks)
            for resp in responses:
                resp.raise_for_status()
                results.extend(resp.json()["results"])
        return results


    async def fetch_all_episodes(self):
        url = f"{self.base_url}/episode"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            results = data["results"]
            total_pages = data["info"]["pages"]

            tasks = [client.get(f"{url}?page={p}") for p in range(2, total_pages + 1)]
            responses = await asyncio.gather(*tasks)
            for resp in responses:
                resp.raise_for_status()
                results.extend(resp.json()["results"])
        return results
