import enum

from django.db import models


# Create your models here.
@enum.unique
class VanillaEnum(enum.Enum):
    RED = enum.auto()
    BLUE = enum.auto()
    GREEN = enum.auto()

    @classmethod
    def choices(cls):
        return tuple((x, x) for x in cls)


class DjangoModel(models.Model):
    name = models.CharField(max_length=20)
    vanilla_enum = models.CharField(choices=VanillaEnum.choices(), default=VanillaEnum.GREEN, max_length=20)

    def __str__(self):
        return f'name={self.name}, vanilla_enun={self.vanilla_enum}'
