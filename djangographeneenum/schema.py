import graphene
from graphene_django import DjangoObjectType

from djangographeneenum.models import DjangoModel, VanillaEnum

ConvertedEnum = graphene.Enum.from_enum(VanillaEnum)


class GrapheneEnum(graphene.Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class GrapheneObject(graphene.ObjectType):
    name = graphene.String()
    converted_enum = graphene.Field(ConvertedEnum)
    graphene_enum = graphene.Field(GrapheneEnum)

    def __str__(self):
        return f'name={self.name}, converted_enum={self.converted_enum}, graphene_enum={self.graphene_enum}'


class DjangoObject(DjangoObjectType):
    class Meta:
        model = DjangoModel


class Query(graphene.ObjectType):
    graphene_object = graphene.Field(GrapheneObject)
    django_model = graphene.List(DjangoObject)

    def resolve_graphene_object(self, info):
        graphene_object = GrapheneObject(name='Abc', converted_enum=ConvertedEnum.RED, graphene_enum=GrapheneEnum.BLUE)
        print(f'graphene_object: {graphene_object}')
        return graphene_object

    def resolve_django_model(self, info):
        django_model = DjangoModel.objects.get_or_create(name='RED Model', vanilla_enum=VanillaEnum.RED)
        print(f'django_model: {django_model}')
        django_model = DjangoModel.objects.get_or_create(name='BLUE Model', vanilla_enum=VanillaEnum.BLUE)
        print(f'django_model: {django_model}')
        django_model = DjangoModel.objects.get_or_create(name='GREEN Model', vanilla_enum=VanillaEnum.GREEN)
        print(f'django_model: {django_model}')
        objects_all = DjangoModel.objects.all()
        for x in objects_all:
            print(f'django_model: {x}')
        return objects_all
