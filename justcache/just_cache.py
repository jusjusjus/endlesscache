
def just_cache(maxsize=1024):

    def _just_cache(func):
        cache = {}
        def wrapped(*args, **kwargs):
            input_str = str(args).replace(' ', '_')+str(kwargs).replace(' ', '_')
            if input_str not in cache:
                res = func(*args, **kwargs)
                if len(cache) < maxsize:
                    cache[input_str] = res
            else:
                res = cache[input_str]
            return res
        
        return wrapped

    return _just_cache


if __name__ == '__main__':
    import time

    def timit(func):

        def wrapped(*args, **kwargs):
            t0 = time.time()
            res = func(*args, **kwargs)
            print(time.time()-t0)
            return res

        return wrapped

    @timit
    @just_cache(maxsize=5)
    def test_func(x, const=5):
        import time
        time.sleep(0.1)
        return x+const

    for i in range(10):
        test_func(5, const=i)
    for i in range(10):
        test_func(5, const=i)
