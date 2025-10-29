"""Drip target sink class, which handles writing streams."""

from __future__ import annotations

import backoff
import requests
from singer_sdk.exceptions import FatalAPIError, RetriableAPIError

from target_hotglue.client import HotglueSink


from target_drip.auth import DripAuthenticator


class DripSink(HotglueSink):
    """Drip target sink class."""

    @property
    def base_url(self) -> str:
        base_url = "https://api.getdrip.com/v2"
        return base_url
    
    @property
    def authenticator(self):
        return DripAuthenticator(self._target, dict())