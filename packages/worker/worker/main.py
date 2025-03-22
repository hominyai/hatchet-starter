from typing import Any

from anyio import run
from hatchet_sdk import ClientConfig, Context
from hatchet_sdk.v2.hatchet import Hatchet

from .settings import settings

hatchet = Hatchet(
    debug=settings.debug,
    config=ClientConfig(
        token=settings.token.get_secret_value(),
        worker_healthcheck_enabled=settings.worker_healthcheck_enabled,
        worker_healthcheck_port=settings.worker_healthcheck_port,
    ),
)

@hatchet.workflow(name="echo")
class EchoWorkflow:
    @hatchet.step()
    async def echo(self, context: Context) -> dict[str, Any]:
        return context.workflow_input()


worker = hatchet.worker(settings.name)

worker.register_workflow(EchoWorkflow())


async def main() -> None:
    await worker.async_start()


if __name__ == "__main__":
    run(main)
