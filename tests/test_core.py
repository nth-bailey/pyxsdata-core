from dataclasses import dataclass, field

import pytest
import pyxsdata_core
from pyxsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class Item:
    id: str = field(metadata={"type": "Attribute"})
    name: str = field(default="")
    count: int = field(default=0)
    score: float = field(default=0.0)
    active: bool = field(default=False)
    created: XmlDate | None = field(default=None)


@dataclass
class Container:
    items: list[Item] = field(
        default_factory=list, metadata={"name": "item", "type": "Element"}
    )
    tag: str = field(default="")


@dataclass
class PriceWithCurrency:
    currency: str = field(metadata={"type": "Attribute"})
    value: float = field(metadata={"type": "Text"})


def test_basic_deserialization():
    xml = b"""
    <Container>
        <tag>electronics</tag>
        <item id="1">
            <name>Keyboard</name>
            <count>42</count>
            <score>9.5</score>
            <active>true</active>
            <created>2024-05-15</created>
        </item>
        <item id="2">
            <name>Mouse</name>
            <count>10</count>
            <score>8.2</score>
            <active>false</active>
            <created>2024-06-20</created>
        </item>
    </Container>
    """
    res = pyxsdata_core.deserialize(xml, Container)
    assert res.tag == "electronics"
    assert len(res.items) == 2

    item1 = res.items[0]
    assert item1.id == "1"
    assert item1.name == "Keyboard"
    assert item1.count == 42
    assert item1.score == 9.5
    assert item1.active is True
    assert item1.created == XmlDate(2024, 5, 15)

    item2 = res.items[1]
    assert item2.id == "2"
    assert item2.name == "Mouse"
    assert item2.count == 10
    assert item2.score == 8.2
    assert item2.active is False
    assert item2.created == XmlDate(2024, 6, 20)


def test_text_field():
    xml = b"""<PriceWithCurrency currency="USD">199.99</PriceWithCurrency>"""
    res = pyxsdata_core.deserialize(xml, PriceWithCurrency)
    assert res.currency == "USD"
    assert res.value == 199.99


def test_empty_container():
    xml = b"""<Container><tag>empty</tag></Container>"""
    res = pyxsdata_core.deserialize(xml, Container)
    assert res.tag == "empty"
    assert res.items == []


@dataclass
class Child:
    name: str = field(default="")
    age: int = field(default=0)


@dataclass
class Parent:
    child: Child | None = field(default=None)
    numbers: list[int] = field(
        default_factory=list, metadata={"name": "num", "type": "Element"}
    )


def test_nested_dataclass_and_primitive_list():
    xml = b"""
    <Parent>
        <child>
            <name>Alice</name>
            <age>12</age>
        </child>
        <num>10</num>
        <num>20</num>
        <num>30</num>
    </Parent>
    """
    res = pyxsdata_core.deserialize(xml, Parent)
    assert res.child is not None
    assert res.child.name == "Alice"
    assert res.child.age == 12
    assert res.numbers == [10, 20, 30]


def test_self_closing_elements():
    @dataclass
    class Node:
        val: str = field(default="default")
        count: int = field(default=99)

    xml = b"""<Node><val/></Node>"""
    res = pyxsdata_core.deserialize(xml, Node)
    assert res.val == ""
    assert res.count == 99


def test_malformed_xml():
    xml = b"""<Container><tag>unclosed"""
    with pytest.raises(ValueError):
        pyxsdata_core.deserialize(xml, Container)


def test_pydantic_model_deserialization():
    from pydantic import BaseModel
    from pyxsdata.pydantic.fields import field as pydantic_field

    class PydanticItem(BaseModel):
        id: str = pydantic_field(metadata={"type": "Attribute"})
        name: str = pydantic_field(default="")
        price: float = pydantic_field(default=0.0)

    class PydanticCart(BaseModel):
        items: list[PydanticItem] = pydantic_field(
            default_factory=list, metadata={"name": "item", "type": "Element"}
        )
        user: str = pydantic_field(default="")

    xml = b"""
    <PydanticCart>
        <user>Alice</user>
        <item id="i1">
            <name>Keyboard</name>
            <price>99.50</price>
        </item>
        <item id="i2">
            <name>Mouse</name>
            <price>24.99</price>
        </item>
    </PydanticCart>
    """
    res = pyxsdata_core.deserialize(xml, PydanticCart)
    assert isinstance(res, PydanticCart)
    assert res.user == "Alice"
    assert len(res.items) == 2
    assert res.items[0].id == "i1"
    assert res.items[0].name == "Keyboard"
    assert res.items[0].price == 99.50
    assert res.items[1].id == "i2"
    assert res.items[1].name == "Mouse"
    assert res.items[1].price == 24.99


def test_str_input():
    xml_str = "<Container><tag>from_str</tag></Container>"
    res = pyxsdata_core.deserialize(xml_str, Container)
    assert res.tag == "from_str"
    assert res.items == []


def test_xml_datetime():
    @dataclass
    class Event:
        timestamp: XmlDateTime = field(metadata={"type": "Element"})

    xml = b"<Event><timestamp>2024-05-15T14:30:00Z</timestamp></Event>"
    res = pyxsdata_core.deserialize(xml, Event)
    assert isinstance(res.timestamp, XmlDateTime)
    assert res.timestamp.year == 2024
    assert res.timestamp.month == 5
    assert res.timestamp.day == 15


def test_boolean_numeric_and_invalid():
    @dataclass
    class Flags:
        flag_one: bool = field(metadata={"type": "Element"})
        flag_zero: bool = field(metadata={"type": "Element"})

    xml = b"<Flags><flag_one>1</flag_one><flag_zero>0</flag_zero></Flags>"
    res = pyxsdata_core.deserialize(xml, Flags)
    assert res.flag_one is True
    assert res.flag_zero is False

    with pytest.raises(ValueError, match="Invalid boolean"):
        pyxsdata_core.deserialize(
            b"<Flags><flag_one>not_a_bool</flag_one><flag_zero>0</flag_zero></Flags>",
            Flags,
        )


def test_invalid_conversions():
    @dataclass
    class Numbers:
        int_val: int = field(metadata={"type": "Element"})
        float_val: float = field(metadata={"type": "Element"})

    with pytest.raises(ValueError, match="Invalid integer"):
        pyxsdata_core.deserialize(
            b"<Numbers><int_val>abc</int_val><float_val>1.5</float_val></Numbers>",
            Numbers,
        )

    with pytest.raises(ValueError, match="Invalid float"):
        pyxsdata_core.deserialize(
            b"<Numbers><int_val>10</int_val><float_val>xyz</float_val></Numbers>",
            Numbers,
        )


def test_version():
    assert isinstance(pyxsdata_core.__version__, str)
    assert len(pyxsdata_core.__version__) > 0
