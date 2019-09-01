import graphene
import graphql_jwt
import django_graphql_movies.schema_relay
import django_graphql_movies.users.schema
import django_graphql_movies.movies.schema

class Query(django_graphql_movies.users.schema.Query, django_graphql_movies.movies.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(django_graphql_movies.movies.schema.Mutation, django_graphql_movies.users.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)