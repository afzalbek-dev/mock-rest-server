import time
import random
from typing import Dict, Any, List, Optional, Tuple
from .generator import SchemaDataGenerator


class MockRESTEngine:
    """Xotirada ishlovchi, CRUD operatsiyalarini taqdim etuvchi Mock REST dvigateli."""

    def __init__(
        self,
        resource_name: str,
        schema: Dict[str, str],
        initial_count: int = 5,
        delay_ms: float = 0.0,
        error_rate: float = 0.0,
    ):
        self.resource_name = resource_name
        self.schema = schema
        self.delay_ms = delay_ms
        self.error_rate = error_rate
        self.items: Dict[int, Dict[str, Any]] = {}
        self._next_id = 1

        for rec in SchemaDataGenerator.generate_initial_data(schema, initial_count):
            rid = rec.get("id", self._next_id)
            self.items[rid] = rec
            self._next_id = max(self._next_id, rid + 1)

    def _simulate_network(self) -> Optional[Tuple[int, str]]:
        if self.delay_ms > 0:
            time.sleep(self.delay_ms / 1000.0)
        if self.error_rate > 0 and random.random() < self.error_rate:
            return 500, "Simulated 500 Internal Server Error (Chaos Test)"
        return None

    def list_items(self) -> Tuple[int, Any]:
        err = self._simulate_network()
        if err:
            return err
        return 200, list(self.items.values())

    def get_item(self, item_id: int) -> Tuple[int, Any]:
        err = self._simulate_network()
        if err:
            return err
        if item_id in self.items:
            return 200, self.items[item_id]
        return 404, {"error": "Not Found", "id": item_id}

    def create_item(self, data: Dict[str, Any]) -> Tuple[int, Any]:
        err = self._simulate_network()
        if err:
            return err
        new_id = self._next_id
        self._next_id += 1
        item = dict(data)
        item["id"] = new_id
        self.items[new_id] = item
        return 201, item

    def update_item(self, item_id: int, data: Dict[str, Any]) -> Tuple[int, Any]:
        err = self._simulate_network()
        if err:
            return err
        if item_id not in self.items:
            return 404, {"error": "Not Found", "id": item_id}
        self.items[item_id].update(data)
        self.items[item_id]["id"] = item_id
        return 200, self.items[item_id]

    def delete_item(self, item_id: int) -> Tuple[int, Any]:
        err = self._simulate_network()
        if err:
            return err
        if item_id in self.items:
            del self.items[item_id]
            return 204, {}
        return 404, {"error": "Not Found", "id": item_id}
