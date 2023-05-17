import httpx
from prefect import flow

@flow
async def get_user_info(username):
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(f"https://api.github.com/users/{username}")
        resp.raise_for_status()

    return resp.json()

