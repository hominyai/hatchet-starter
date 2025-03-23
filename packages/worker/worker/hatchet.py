from typing import Any

from hatchet_sdk import ClientConfig
from hatchet_sdk.v2.hatchet import Hatchet

from .settings import settings

__all__ = ("hatchet", "worker")

hatchet = Hatchet(
    debug=settings.debug,
    config=ClientConfig(
        token=settings.token.get_secret_value(),
        worker_healthcheck_enabled=settings.worker_healthcheck_enabled,
        worker_healthcheck_port=settings.worker_healthcheck_port,
    ),
)

from .workflows import EchoWorkflow

worker = hatchet.worker(settings.name)

worker.register_workflow(EchoWorkflow())
