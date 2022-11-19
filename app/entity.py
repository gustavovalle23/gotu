# -*- coding: utf-8 -*-
from app.field import Field
from app.base_entity import BaseEntity


class EntityBuilder:
    def __init__(self, name, body: dict) -> None:
        self.name = name
        self.body = body

    def build(self):
        ...


def entity(name, body):
    builder = EntityBuilder(name, body)
    return builder.build()


setattr(entity, "is_entity", isinstance(BaseEntity))
