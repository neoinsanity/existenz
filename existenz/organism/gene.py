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


class CharGene(BaseGene):
    MUTATION_AMOUNT = 1
    RAND_MAX_DEFAULT = '\xff'
    RAND_MIN_DEFAULT = '\x00'

    ONTIC_SCHEMA = deepcopy(BaseGene.ONTIC_SCHEMA)
    ONTIC_SCHEMA.update(SchemaType(
        mut_amt={
            'type': int,
            'required': True,
            'default': MUTATION_AMOUNT,
        },
        rand_max={
            'type': str,
            'required': True,
            'default': RAND_MAX_DEFAULT,
            'min': 1,
            'max': 1,
        },
        rand_min={
            'type': str,
            'required': True,
            'default': RAND_MIN_DEFAULT,
            'min': 1,
            'max': 1,
        },
        value={
            'type': basestring,
            'default': None,
            'min': 1,
            'max': 1,
        }
    ))


class IntGene(BaseGene):
    MUTATION_AMOUNT = 1
    RAND_MAX_DEFAULT = sys.maxint
    RAND_MIN_DEFAULT = -sys.maxint - 1

    ONTIC_SCHEMA = deepcopy(BaseGene.ONTIC_SCHEMA)
    ONTIC_SCHEMA.update(SchemaType(
        mut_amt={
            'type': int,
            'required': True,
            'default': MUTATION_AMOUNT,
        },
        rand_max={
            'type': int,
            'required': True,
            'default': RAND_MAX_DEFAULT,
        },
        rand_min={
            'type': int,
            'required': True,
            'default': RAND_MIN_DEFAULT,
        },
        value={
            'type': int,
        }
    ))

    def __init__(self, *args, **kwargs):
        BaseGene.__init__(self, *args, **kwargs)
