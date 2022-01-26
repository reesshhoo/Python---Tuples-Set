
def myreduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value=initializer
    for i in it:
        value = function(value, i)
    return value


