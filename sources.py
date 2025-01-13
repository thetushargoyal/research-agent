
class Source:
    url = None
    source_type = None

    def __init__(self, url, source_type):
        self.url = url
        self.source_type = source_type

arvix_lite = Source("https://arxiv-sanity-lite.com/", 
                    "research_paper")

google_scholar = Source("https://scholar.google.com/",
                        "search_engine")