def grouper(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]
