# -*- coding: utf-8 -*-
from src.entity import entity
from src.field import field


def test_should_seila():
    entity(
        "List",
        {
            # 'id': identifier(int),
            "name": field(str),
            "description": field(str),
        },
    )
