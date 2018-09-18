from ontic.meta_type import PropertySchema
from ontic.ontic_type import OnticType
from ontic.schema_type import SchemaType


ENTITY_TYPE = {'plant'}

class Entity(OnticType):
    ONTIC_SCHEMA = SchemaType(
        id=PropertySchema(required=True, type=int),
        type=PropertySchema(required=True, type=str, enum=ENTITY_TYPE),
    )

    def life_cycle(self, world, location):
        neighbors = world.get_neighbors(location.x, location.y)
        plant_count = 0
        for loc in neighbors:
            if loc.has_type(self.type):
                plant_count += 1
