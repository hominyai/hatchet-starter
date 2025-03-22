from pathlib import PurePath

from pydantic import AliasChoices, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="x_hatchet_client_")
    secrets_dir: PurePath = Field(default_factory=lambda: PurePath("/run/secrets"))


_settings = _Settings()


class HatchetSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="hatchet_client_",
        env_ignore_empty=True,
        secrets_dir=str(_settings.secrets_dir),
    )

    debug: bool = False

    name: str = Field(validation_alias=AliasChoices("hostname"))
    token: SecretStr
    worker_healthcheck_enabled: bool = True
    worker_healthcheck_port: int = 8002


settings = HatchetSettings()