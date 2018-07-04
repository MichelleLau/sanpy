import iso8601

QUERY_MAPPING = {
    'daily_active_addresses': {
        'query': 'dailyActiveAddresses',
        'return_fields': ['datetime', 'activeAddresses']
    },
    'burn_rate': {
        'query': 'burnRate',
        'return_fields': ['datetime', 'burnRate']
    },
    'transaction_volume': {
        'query': 'transactionVolume',
        'return_fields': ['datetime', 'transactionVolume']
    },
    'github_activity': {
        'query': 'githubActivity',
        'return_fields': ['datetime', 'activity']
    },
    'prices': {
        'query': 'historyPrice',
        'return_fields': ['datetime', 'priceUsd', 'priceBtc']
    }
}


def daily_active_addresses(idx, slug, **kwargs):
    query_str = _create_query_str('daily_active_addresses', idx, slug, **kwargs)

    return query_str


def burn_rate(idx, slug, **kwargs):
    query_str = _create_query_str('burn_rate', idx, slug, **kwargs)

    return query_str


def transaction_volume(idx, slug, **kwargs):
    query_str = _create_query_str('transaction_volume', idx, slug, **kwargs)

    return query_str


def github_activity(idx, slug, **kwargs):
    query_str = _create_query_str('github_activity', idx, slug, **kwargs)

    return query_str


def prices(idx, slug, **kwargs):
    query_str = _create_query_str('prices', idx, slug, **kwargs)

    return query_str


def projects(idx, slug, **kwargs):
    query_str = """
    query_{idx}: allProjects
    {{
        name,
        slug,
        ticker
    }}
    """.format(idx=idx)

    return query_str


def _create_query_str(query, idx, slug, **kwargs):
    kwargs['from_date'] = _format_date(kwargs['from_date'])
    kwargs['to_date'] = _format_date(kwargs['to_date'])

    query_str = """
    query_{idx}: {query}(
        slug: \"{slug}\",
        from: \"{from_date}\",
        to: \"{to_date}\",
        interval: \"{interval}\"
    ){{
        {return_fields}
    }}
    """.format(
        query=QUERY_MAPPING[query]['query'],
        idx=idx,
        slug=slug,
        return_fields=_format_return_fields(QUERY_MAPPING[query]['return_fields']),
        **kwargs
    )

    return query_str


def _format_return_fields(return_fields):
    return ",\n".join(return_fields)


def _format_date(date_str):
    return iso8601.parse_date(date_str).isoformat()


def _result_curr(curr_to):
    return "price" + curr_to.title()
