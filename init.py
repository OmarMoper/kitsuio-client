import kitsu

client = kitsu.KitsuClient()
args = {
    'filter': {'genres': 'action'},
    'sort': ['endDate', '-episodeCount'],
    'page': {'limit': 2}
}
