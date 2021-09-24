import graphene
from graphene_django import DjangoObjectType
from .models import Books


# describe our data models that we are going to provide to graphql server

class BooksType(DjangoObjectType):
    # DjangoObjectType: we taking out data and formatting that into a type that can be utilize and use.
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")


class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)

    def resolve_all_books(root, info):
        return Books.objects.filter(title="Dini")


schema = graphene.Schema(query=Query)
