import base64
import logging

from target_hotglue.auth import Authenticator

class DripAuthenticator(Authenticator):
    """API Authenticator for OAuth 2.0 flows."""
    
    def __init__(self, target, state):
        super().__init__(target, state)
        # Fallback logger if not present on target
        self.logger = getattr(target, 'logger', logging.getLogger(__name__))
        self._config_file_path = getattr(target, '_config_file_path', None)

    @property
    def auth_headers(self) -> dict:
        result = {}
        api_key = base64.b64encode(f"{self._config.get('api_key')}:".encode('utf-8'))
        result["Authorization"] = f"Basic {api_key.decode('utf-8')}"
        return result