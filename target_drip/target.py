"""Drip target class."""

from __future__ import annotations

from singer_sdk import typing as th
from target_hotglue.target import TargetHotglue

from target_drip.sinks import (
    EventsSink,
)


class TargetDrip(TargetHotglue):
    """Sample target for Drip."""

    name = "target-drip"

    def __init__(
        self,
        config=None,
        parse_env_config: bool = False,
        validate_config: bool = True,
        state: str = None
    ) -> None:
        self.config_file = config[0]
        super().__init__(config, parse_env_config, validate_config, state)

    SINK_TYPES = [EventsSink]
    MAX_PARALLELISM = 1

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
        th.Property("account_id", th.StringType, required=True),
    ).to_dict()


if __name__ == "__main__":
    TargetDrip.cli()
