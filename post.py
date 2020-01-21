from markdown2 import markdown as mdwn 
from datetime import datetime
import os

class Post:
    def __init__(self, path_to_source : str):
        with open(path_to_source) as f:
            prepend = f.read().split('---')[1:]
            for i in f.read():
                c = 0
                if i == ' ':
                    c += 1
                if c == 30:
                    source = prepend()[:i]
            source[:teaserlen]
            self.html = mdwn(f.read(), extras=["metadata"])
            self.metadata = self.html.metadata
            # Link is a filename without the markdown extension
            # os.path.split('/home/ellie') => ['/home', 'ellie']
            # os.psth.splittext('/home/somfile.txt') => ['/home/somefile', 'txt']
            self.link = f"{os.path.splitext(os.path.split(path_to_source)[-1])[0]}"

    def __str__(self) -> str:
        return self.source

