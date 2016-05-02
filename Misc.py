def flatten(list):
    return [item for sublist in list for item in sublist]

def find(item, list):
    return next(x for x in list if item in x.names)
