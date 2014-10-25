from copy import deepcopy
import sys

from ontic.ontic_type import OnticType, perfect_object
from ontic.schema_type import PropertySchema, SchemaType


class BaseGene(OnticType):
    ONTIC_SCHEMA = SchemaType(
        mut_prob=PropertySchema(
            type=float,
            default=0.01),
        value=PropertySchema())

    def __init__(self, *args, **kwargs):
        OnticType.__init__(self, *args, **kwargs)
        perfect_object(self)

    def mutate(self):
        """Causes the gene to mutate."""
        raise NotImplementedError('Must be implemented by subclasses.')

    def random_value(self):
        """Generate a plausible random value for a given gene type."""
        raise NotImplementedError('Must be implemented by subclasses.')




class CharGene(BaseGene):
    MUTATION_AMOUNT = 1
    RAND_MAX_DEFAULT = '\xff'
    RAND_MIN_DEFAULT = '\x00'

    ONTIC_SCHEMA = deepcopy(BaseGene.ONTIC_SCHEMA)
    ONTIC_SCHEMA.update(SchemaType(
        mut_amt=PropertySchema(
            type=int,
            required=True,
            default=MUTATION_AMOUNT),
        rand_max=PropertySchema(
            type=str,
            required=True,
            default=RAND_MAX_DEFAULT,
            min=1,
            max=1),
        rand_min=PropertySchema(
            type=str,
            required=True,
            default=RAND_MIN_DEFAULT,
            min=1,
            max=1),
        value=PropertySchema(
            type=basestring,
            default=None,
            min=1,
            max=1)
    ))


class IntGene(BaseGene):
    MUTATION_AMOUNT = 1
    RAND_MAX_DEFAULT = sys.maxint
    RAND_MIN_DEFAULT = -sys.maxint - 1

    ONTIC_SCHEMA = deepcopy(BaseGene.ONTIC_SCHEMA)
    ONTIC_SCHEMA.update(SchemaType(
        mut_amt=PropertySchema(
            type=int,
            required=True,
            default=MUTATION_AMOUNT),
        rand_max=PropertySchema(
            type=int,
            required=True,
            default=RAND_MAX_DEFAULT),
        rand_min=PropertySchema(
            type=int,
            required=True,
            default=RAND_MIN_DEFAULT
        ),
        value=PropertySchema(
            type=int)
    ))
