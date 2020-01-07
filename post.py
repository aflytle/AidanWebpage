from markdown2 import markdown as mdwn 
from datetime import datetime


class Post:
    def __init__(self, path_to_source : str):
        with open(path_to_source) as f:
            return mdwn(f.read(), extras=["metadata"])
            

    def __str__(self) -> str:
        return self.source



