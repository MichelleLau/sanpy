import pandas as pd
import san.sanbase_graphql
from san.graphql import execute_gql
from san.error import SanError


def get(dataset, **kwargs):
    gql_query = get_gql_query(0, dataset, **kwargs)
    gql_query = "{\n" + gql_query + "\n}"
    res = execute_gql(gql_query)
    print(res)
    df = pd.DataFrame(res["query_0"])
    return df


def get_gql_query(idx, dataset, **kwargs):
    query, slug = _parse_dataset(dataset)
    return getattr(
        san.sanbase_graphql,
        query,
        lambda *args, **kwargs: not_found(query)
        )(idx, slug, **kwargs)


def _parse_dataset(dataset):
    return dataset.split("/")


def not_found(query):
    raise SanError(query + ' not found')
