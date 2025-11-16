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
        "all": "0",
        "movies": "1",
        "tv": "2",
        "music": "3",
        "games": "4",
        "books": "5",
        "software": "6",
        "adult": "7",
    }

    def __init__(self):
        return

    def download_torrent(self, info):
        return

    def search(self, what, cat="all"):
        return
