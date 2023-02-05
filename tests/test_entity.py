# -*- coding: utf-8 -*-
from src.entity import entity
from src.field import field


def test_should_instantiate_an_entity():
    User = entity(
        "User",
        {
            "name": field(str),
            "age": field(int),
        },
    )
    user = User.from_json({"name": "Gustavo", "age": 23})

    assert user.name == "Gustavo"
    assert user.age == 23

    assert User.is_entity(user) == True
