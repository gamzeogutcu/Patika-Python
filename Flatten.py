def flatten(l):
    if not isinstance(l, list):
        return [l]
    flat = []
    for sublist in l:
        flat.extend(flatten(sublist))
    return flat

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))