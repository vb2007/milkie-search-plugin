# qbittorrent helpers
from helpers import download_file, retrieve_url

# api requests
from requests import get

global base_api_url
base_api_url = "https://milkie.cc/api/v1"
global api_key
# get key from: https://milkie.cc/settings/security
api_key = "your_key_goes_here"


class milkie(object):
    url = base_api_url + "/torrents"
    name = "Milkie"
    supported_categories = {
        "all": "null",
        "movies": "1",
        "tv": "2",
        "music": "3",
        "games": "4",
        "books": "5",
        "software": "6",
        "adult": "7",
    }

    # def __init__(self):
    #    return

    def search(self, what, cat="all"):
        # building the request
        search_url = base_api_url + "/torrents"
        headers = {"x-milkie-auth": api_key}
        params = {
            "query": what,
            "oby": "created_at",
            "odir": "desc",
            "pi": "0",
            "ps": "100",
        }

        # when searching for all categories, appending a "category" param makes the api throw back no results
        if cat != "all":
            params["categories"] = self.supported_categories[cat]

        results = get(url=search_url, params=params, headers=headers)
        if results.status_code == 200:
            torrents = results.json()
            for torrent in torrents:
                print(
                    f"{torrent['download_url']}|"  # link (download URL)
                    f"{torrent['name']}|"  # name
                    f"{torrent.get('size', -1)}|"  # size in bytes (-1 if unknown)
                    f"{torrent.get('seeders', -1)}|"  # seeds
                    f"{torrent.get('leechers', -1)}|"  # leech
                    f"{torrent.get('link', 'https://milkie.cc')}"
                )

    def download_torrent(self, info):
        return download_file(info)
