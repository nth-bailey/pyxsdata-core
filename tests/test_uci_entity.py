import pytest
import pyxsdata_core
from pyxsdata.formats.dataclass.serializers import XmlSerializer

from tests.schemas.uci.generated.uci_message_definitions_v2_5_0 import (
    DateTimeSigmaType,
    Entity,
    EntityIdentityType,
    EntityIdType,
    EntityMdt,
    EntitySourceEnum,
    EntitySourceType,
    EntityStatusEnum,
    HeaderType,
    MessageModeEnum,
    ObjectStateEnum,
    SystemIdType,
)
from tests.schemas.uci.generated.uci_security_markings_v2_5_0 import (
    ClassificationEnum,
    SecurityInformationType,
)


@pytest.fixture
def uci_entity_sample() -> tuple[Entity, bytes]:
    entity = Entity(
        security_information=SecurityInformationType(
            classification=ClassificationEnum.U,
            owner_producer=["USA"],
        ),
        message_header=HeaderType(
            system_id=SystemIdType(uuid="00000000-0000-0000-0000-000000000001"),
            timestamp="2026-09-07T22:00:00Z",
            schema_version="002.5.0",
            mode=MessageModeEnum.LIVE,
        ),
        object_state=ObjectStateEnum.NEW,
        message_data=EntityMdt(
            entity_id=EntityIdType(uuid="00000000-0000-0000-0000-000000000002"),
            creation_timestamp=DateTimeSigmaType(date_time="2026-09-07T22:00:00Z"),
            source=EntitySourceType(
                source_type=EntitySourceEnum.IFF,
                system_id=SystemIdType(uuid="00000000-0000-0000-0000-000000000003"),
            ),
            entity_status=EntityStatusEnum.CONFIRMED,
            identity=EntityIdentityType(identity_timestamp="2026-09-07T22:00:00Z"),
        ),
    )
    xml_str = XmlSerializer().render(entity)
    return entity, xml_str.encode("utf-8")


def test_uci_entity_deserialization(uci_entity_sample: tuple[Entity, bytes]) -> None:
    _original, xml_bytes = uci_entity_sample

    res = pyxsdata_core.deserialize(xml_bytes, Entity)

    assert isinstance(res, Entity)
    assert res.object_state == ObjectStateEnum.NEW
    assert res.message_data.entity_status == EntityStatusEnum.CONFIRMED
    assert res.message_data.entity_id.uuid == "00000000-0000-0000-0000-000000000002"
    assert res.security_information.classification == ClassificationEnum.U
    assert res.message_header.mode == MessageModeEnum.LIVE
    assert res.message_header.schema_version == "002.5.0"
    assert res.message_data.source.source_type == EntitySourceEnum.IFF


def test_uci_entity_benchmark(
    benchmark, uci_entity_sample: tuple[Entity, bytes]
) -> None:
    _, xml_bytes = uci_entity_sample
    res = benchmark(pyxsdata_core.deserialize, xml_bytes, Entity)
    assert isinstance(res, Entity)
