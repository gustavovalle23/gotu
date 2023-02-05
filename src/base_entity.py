# -*- coding: utf-8 -*-
from typing import Any, Dict


class NewObject:
    pass


class BaseEntity:
    meta = {"schema": {}}

    def __init__(self) -> None:
        for name, definition in self.meta.get("schema").items():
            if callable(definition):
                continue

            object.__setattr__(self, name, definition.default_value)

    @staticmethod
    def from_json(json: Dict[str, Any]):
        instance = BaseEntity()
        for key, value in json.items():
            object.__setattr__(instance, key, value)

        return instance
