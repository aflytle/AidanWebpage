import markdown2
from datetime import datetime
from bs4 import BeautifulSoup


class Post:
    def __init__(self, path_to_source : str):
        with open(path_to_source) as f:
            source = f.read()
        raw_text = source.split('-'*10)
        print(raw_text)
        markdown_source = raw_text[1]
        self.title = raw_text[0].split('\n')[0].split(':')[1].strip() # This is Hacky and there's a better solution out there
        self.date = datetime.strptime(raw_text[0].split('\n')[1].split(':')[1].strip(), "%d-%m-%Y").date()
        self.page_source = markdown2.Markdown().convert(markdown_source)
        soup = BeautifulSoup(self.page_source)
        self.link = path_to_source
        self.teaser = ''.join([ str(i) for i in soup.find_all('p')[:2] ])
    
    def __str__(self) -> str:
        return self.source



