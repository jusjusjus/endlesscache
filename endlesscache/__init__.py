def endless_cache(fn):
    cache = {}
    def wrapped(arg):
        try:
            res = cache[arg]
        except:
            res = fn(arg)
            cache[arg] = res
        finally:
            return res
    
    return wrapped
