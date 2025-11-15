from novaprinter import prettyPrinter

class milkie(object):
    url = "https://milkie.cc/api/v1/torrents"
    name = "Milkie"
    supported_categories = {
        "all": "0",
        "movies": "1",
        "tv": "2",
        "music": "3",
        "games": "4",
        "ebooks": "5",
        "apps": "6",
        "adult": "7"
    }
    # get key from: https://milkie.cc/settings/security
    api_key = "your_key_goes_here"

    def authenticate(key):
        try:
            base_url = "https://milkie.cc/api/v1"
            reponse = requests.get(base_url)

    def
