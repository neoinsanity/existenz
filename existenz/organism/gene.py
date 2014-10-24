from copy import deepcopy
import sys

from ontic.ontic_type import OnticType
from ontic.schema_type import SchemaType


class BaseGene(OnticType):
    ONTIC_SCHEMA = SchemaType(
        mut_prob={
            'type': float,
            'default': 0.01,
        },
        value={}
    )

    def __init__(self, *args, **kwargs):
        OnticType.__init__(self, *args, **kwargs)


class IntGene(BaseGene):
    RAND_MAX_DEFAULT = sys.maxint
    RAND_MIN_DEFAULT = -sys.maxint - 1

    ONTIC_SCHEMA = deepcopy(BaseGene.ONTIC_SCHEMA)
    ONTIC_SCHEMA.update(SchemaType({
        'rand_max': {
            'type': int,
            'required': True,
            'default': RAND_MAX_DEFAULT,
        },
        'rand_min': {
            'type': int,
            'required': True,
            'default': RAND_MIN_DEFAULT,
        },
        'value': {
            'type': int,
        },
    }))
