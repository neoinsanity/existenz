"""A location is the representation of a given point on a glove."""

from ontic.meta_type import PropertySchema
from ontic.ontic_type import OnticType
from ontic.schema_type import SchemaType


class Location(OnticType):
    ONTIC_SCHEMA = SchemaType(
        id=PropertySchema(required=True, type=int),
        x=PropertySchema(required=True, type=int),
        y=PropertySchema(required=True, type=int),
        type_count=PropertySchema(required=True, type=dict, default=dict()),
        entities=PropertySchema(required=True, type=dict, default=dict())
    )

    def add_entity(self, entity):
        self.entities[entity.id] = entity
        self.type_count[entity.type] = 1

    def remove_entity(self, entity):
        self.type_count[entity.type] = 0
        del self.entities[entity.id]

    def has_type(self, type):
        return self.type_count.get(type, 0)
