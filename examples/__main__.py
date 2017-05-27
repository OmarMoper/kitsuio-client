"""Basic example about how to use kitsu client."""
import kitsu

client = kitsu.KitsuClient()
args = {
    'filter': {'genres': 'action'},
    'sort': ['endDate', '-episodeCount'],
    'page': {'limit': 2}
}

print(client.get('anime', args))
