from markdown2 import markdown as mdwn 
from datetime import datetime


class Post:
    def __init__(self, path_to_source : str):
        with open(path_to_source) as f:
            f.read = f.read().split('---')[1:]
            for i in f.read():
                c = 0
                if i == ' ':
                    c += 1
                if c == 30:
                    source = f.read()[:i]
            source[:teaserlen]
            self.html = mdwn(f.read(), extras=["metadata"])
            self.metadata = self.html.metadata

    def __str__(self) -> str:
        return self.source



