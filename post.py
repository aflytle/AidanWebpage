from markdown2 import markdown as mdwn
from datetime import datetime
import os

class Post:
    def __init__(self, path_to_source : str):
        # The Structure of our markdown files is as such
        #   
        #   metadata including date and title
        #   ---
        #   body of the post
        #
        # Our goal is to open the markdown file
        # and read in the plaintext metadata and all
        with open(path_to_source) as f:
            fullDoc = f.read()
        # Next we split the text on the first '---' (the metadata seperator)
        # and whats left in the string source
        # We do this to create a teaser to display on
        # the main blog page. and this discards all the metadata
        source = "---".join(fullDoc.split('---')[1:])
        teaser = ""
        # next we use a for loop to grab the first 150 chars, rounding to the
        # next word boundary (" ")
        for i in range(len(source)):
            if i >= 150 and source[i] == " ":
                break
            teaser += source[i]
        # finally we convert the teaser from html to markdown
        self.teaser = mdwn(teaser)
        # we then convert the rest of the document, to html, and parse the metadata
        self.html = mdwn(fullDoc, extras=["metadata"])
        self.metadata = self.html.metadata
        self.date = datetime.strptime(self.metadata['date'], '%d-%m-%Y')
        # self.metadata is a dictionary, and any 'key: value' line prior to 
        # the first '---'

        # Link is a filename without the markdown extension
        # os.path.split('/home/ellie') => ['/home', 'ellie']
        # os.psth.splittext('/home/somfile.txt') => ['/home/somefile', 'txt']
        self.link = f"{os.path.splitext(os.path.split(path_to_source)[-1])[0]}"
        print(f"""
            {self.html}
            {self.metadata}
            {self.teaser}
            {self.link}
        """)
