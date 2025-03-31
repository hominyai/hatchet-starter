import datetime
import logging
import anyio

from .hatchet import hatchet, worker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def _worker() -> None:
    await worker.async_start()


async def _listener() -> None:
    listener = hatchet.listener.stream_by_additional_metadata("e", "*")
    async for event in listener:
        logger.info(f"Received event: type={event.type} payload={event.payload}")

    logger.error("Listener stopped unexpectedly!")


async def _periodic_emitter() -> None:
    while True:
        await hatchet.event.async_push(
            "echo", {"triggered_at": datetime.datetime.now().isoformat()}, {"additional_metadata": {"e": "*"}}
        )
        await anyio.sleep(5)


async def main() -> None:
    async with anyio.create_task_group() as tg:
        tg.start_soon(_worker)
        tg.start_soon(_listener)
        tg.start_soon(_periodic_emitter)


if __name__ == "__main__":
    anyio.run(main)
