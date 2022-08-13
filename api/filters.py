import django_filters
from .models import *

class MediumFilter(django_filters.FilterSet):
    having_medium = django_filters.Filter(name="mediums", lookup_type='in')

    class Meta:
        model = Artwork