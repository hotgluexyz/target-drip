"""Drip target sink class, which handles writing streams."""

from __future__ import annotations

from __future__ import annotations



from target_drip.client import DripSink

class EventsSink(DripSink):
    """Drip target sink class."""
    name = "Events"
    
    @property
    def endpoint(self) -> str:
        return f"/{self.config.get('account_id')}/events"
    
    def preprocess_record(self, record: dict, context: dict) -> dict:
        return record
    
    def upsert_record(self, record: dict, context: dict):
        events = {
            "events": [record]
        }
        response = self.request_api("POST", request_data=events) # returns 204 no content
        id = record.get("id", record.get("email"))
        return id, response.ok, dict()

class SubscribersSink(DripSink):
    """Drip target sink class."""
    name = "Subscribers"
    
    @property
    def endpoint(self) -> str:
        return f"/{self.config.get('account_id')}/subscribers"
    
    def preprocess_record(self, record: dict, context: dict) -> dict:
        return record
    
    def upsert_record(self, record: dict, context: dict):
        subscribers = {
            "subscribers": [record]
        }
        response = self.request_api("POST", request_data=subscribers) # returns 204 no content
        id = response.json().get("subscribers")[0].get("id")
        return id, response.ok, dict()