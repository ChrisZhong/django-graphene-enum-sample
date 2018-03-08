import graphene

import djangographeneenum.schema


class Query(djangographeneenum.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
