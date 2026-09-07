# Quickstart

Get up and running with `pyxsdata-core` in minutes.

---

## 1. Installation

Install `pyxsdata-core` via `uv` or `pip`:

=== "uv"

    ```console
    $ uv add pyxsdata-core
    ```

=== "pip"

    ```console
    $ pip install pyxsdata-core
    ```

Pre-compiled binary wheels are available for Linux, macOS, and Windows. No Rust compiler is required for standard installations.

---

## 2. Deserializing Models

`pyxsdata-core` provides a single high-level function, `pyxsdata_core.deserialize()`, which accepts XML raw bytes or strings and a target Python class.

### Working with Pydantic v2

Pydantic v2 `BaseModel` classes are supported natively. You can use standard field annotations, defaults, and field metadata:

```python
from pydantic import BaseModel, Field
import pyxsdata_core

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Customer(BaseModel):
    id: int
    name: str
    email: str | None = None
    address: Address

xml = b"""
<Customer>
    <id>1001</id>
    <name>Jane Doe</name>
    <email>jane@example.com</email>
    <address>
        <street>123 Innovation Way</street>
        <city>San Francisco</city>
        <zip_code>94107</zip_code>
    </address>
</Customer>
"""

customer = pyxsdata_core.deserialize(xml, Customer)
print(customer)
# Customer(id=1001, name='Jane Doe', email='jane@example.com', address=Address(...))
print(type(customer.address))
# <class '__main__.Address'>
```

### Working with Standard Library Dataclasses

`pyxsdata-core` also deserializes standard Python `@dataclass` objects with nested children, collections, and optional fields:

```python
from dataclasses import dataclass, field
import pyxsdata_core

@dataclass
class LineItem:
    sku: str
    quantity: int
    price: float

@dataclass
class Order:
    order_id: str
    items: list[LineItem] = field(default_factory=list)

xml = b"""
<Order>
    <order_id>ORD-9874</order_id>
    <items>
        <sku>A1</sku>
        <quantity>2</quantity>
        <price>14.50</price>
    </items>
    <items>
        <sku>B2</sku>
        <quantity>1</quantity>
        <price>99.00</price>
    </items>
</Order>
"""

order = pyxsdata_core.deserialize(xml, Order)
print(f"Order {order.order_id} has {len(order.items)} line items:")
for item in order.items:
    print(f"  - {item.quantity}x {item.sku} @ ${item.price}")
```

---

## 3. Precompiling Schemas with `ModelSchema`

For maximum performance in hot loops, you can precompile the class schema once and reuse it across multiple deserialization calls:

```python
from pyxsdata_core import ModelSchema

# Compile class structure into Rust schema registry once
schema = ModelSchema(Customer)

# Reuse compiled schema across thousands of messages
for raw_xml in message_stream:
    customer = schema.deserialize(raw_xml)
    process(customer)
```

Precompiling eliminates Python reflection and field inspection on every document, achieving maximum sustained throughput.
