# -*- coding: utf-8 -*-
class Field:
    def __init__(self, type, options: dict = None) -> None:
        if options is None:
            options = dict()

        self.name = ""
        self.type = type
        self.options = options
        self._validations = None

    @property
    def default_value(self):
        if self.options.get("default") is not None:
            if callable(self.options.get("default")):
                return self.options.get("default")()
            return self.options.get("default")

    @property
    def validation(self):
        if self._validations:
            return self._validations

        validation = {"type": self.type}

        if self.options.get("validation"):
            validation.update(self.options.get("validation"))

        self._validations = validation
        return self._validations


def field(type, options):
    return Field(type, options)
