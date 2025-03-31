import json
import logging
from typing import Any

from hatchet_sdk import Context

from ..hatchet import hatchet

logger = logging.getLogger(__name__)

@hatchet.workflow(name="echo", on_events=["echo"])
class EchoWorkflow:
    @hatchet.step()
    async def echo(self, context: Context) -> dict[str, Any]:
        input = json.dumps(context.workflow_input())
        metadata = context.additional_metadata()

        logger.info(f"EchoWorkflow running: input={input} metadata={metadata}")
        context.put_stream(input)
        return context.workflow_input()
