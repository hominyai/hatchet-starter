from anyio import run

from .hatchet import hatchet, worker


async def main() -> None:
    await hatchet.event.async_push("echo", {"caller": __name__})
    await worker.async_start()


if __name__ == "__main__":
    run(main)
