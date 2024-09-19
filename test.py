import asyncio
import aiohttp

async def test_recommendation():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://localhost:8000/api/recommend",
            json={"user_id": "test_user", "query": "I need a new smartphone with a good camera"}
        ) as response:
            print(await response.json())

asyncio.run(test_recommendation())