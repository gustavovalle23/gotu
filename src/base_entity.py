# -*- coding: utf-8 -*-
class BaseEntity:
    def __init__(self) -> None:
        for name, definition in self.meta.schema:
            self[name] = definition.default_value
