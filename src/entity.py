# -*- coding: utf-8 -*-
from typing import Dict, Any
import inspect

from src.field import Field
from src.base_entity import BaseEntity


class EntityBuilder:
    def __init__(self, name: str, body: dict) -> None:
        self.name = name
        self.body = body

    def build(self):
        Entity = type(self.name, (BaseEntity,), {})

        Entity.meta = {"name": self.name, "schema": {}}

        for name, info in self.body.items():
            if not isinstance(info, Field):
                object.__setattr__(Entity, name, info)
                Entity.meta.get("schema")[name] = lambda: None
                continue

            info.name = name
            Entity.meta.get("schema")[name] = info
        return Entity


def entity(name: str, body: Dict[str, Any]):
    builder = EntityBuilder(name, body)

    entity_build = builder.build()
    entity_build.is_entity = lambda instance: isinstance(instance, BaseEntity)
    return entity_build
