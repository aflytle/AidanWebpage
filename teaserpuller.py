def teaserpuller(md):
    opnd = open(md, "r")
    title = opnd[1] # add slice on colon
    date = opnd[2] # add slice on colon
    teaser = opnd[4:5]
    return title, date, teaser
