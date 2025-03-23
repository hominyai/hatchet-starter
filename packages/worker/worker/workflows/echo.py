from typing import Any

from hatchet_sdk import Context

from ..hatchet import hatchet


@hatchet.workflow(name="echo", on_events=["echo"])
class EchoWorkflow:
    @hatchet.step()
    async def echo(self, context: Context) -> dict[str, Any]:
        return context.workflow_input()
