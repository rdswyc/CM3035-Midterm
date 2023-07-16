from django.conf import settings
from random import choices, randint
import factory

from .models import *
from .serializers import *

class OrganismFactory(factory.django.DjangoModelFactory):
    taxa_id = randint(1, 100000)
    clade = 'E'
    genus = factory.Faker('last_name')
    species = factory.Faker('name')

    class Meta:
        model = Organism

class ProteinFactory(factory.django.DjangoModelFactory):
    protein_id = hex(randint(1, 100000))[2:]
    length = randint(1, 1000)
    organism = factory.SubFactory(OrganismFactory)

    class Meta:
        model = Protein

class SequenceFactory(factory.django.DjangoModelFactory):
    protein = factory.SubFactory(ProteinFactory)
    sequence = ''.join(choices(settings.AMINOACIDS, k=randint(1, 1000)))

    class Meta:
        model = Sequence

class PfamFactory(factory.django.DjangoModelFactory):
    pfam_id = hex(randint(1, 100000))[2:]
    description = factory.Faker('sentence', nb_words=2)

    class Meta:
        model = Pfam

class DomainFactory(factory.django.DjangoModelFactory):
    protein = factory.SubFactory(ProteinFactory)
    pfam = factory.SubFactory(PfamFactory)
    description = factory.Faker('sentence', nb_words=2)
    start = randint(1, 500)
    stop = randint(501, 1000)

    class Meta:
        model = Domain


class ProteinSerializerFactory(factory.DictFactory):
    protein_id = ProteinFactory.build().protein_id
    sequence = SequenceFactory.build().sequence
    taxonomy = organism = OrganismFactory.build().__dict__
    length = len(sequence)
    domains = [{
        **d.__dict__,
        'pfam_id': {
            'domain_id': PfamFactory.build().pfam_id,
            'domain_description': PfamFactory.build().description
        }
    } for d in DomainFactory.build_batch(3)]