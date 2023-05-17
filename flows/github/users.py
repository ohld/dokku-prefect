import httpx
from prefect import flow, task, get_run_logger

@task
async def get_user_info(username: str) -> dict:
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(f"https://api.github.com/users/{username}")
        resp.raise_for_status()

    return resp.json()


@flow
async def analyse_github_user(username: str):
    github_user_info = await get_user_info(username)

    logger = get_run_logger()
    logger.info(f"""@{username}'s id = {github_user_info["id"]}""")
