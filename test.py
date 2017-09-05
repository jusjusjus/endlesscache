
from endlesscache import endless_cache

import time

def timit(func):

    def wrapped(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        print(time.time()-t0)
        return res

    return wrapped

@timit
@endless_cache
def test_func(x):
    import time
    time.sleep(0.1)
    return x*5

for i in range(10):
    print(test_func(i))
for i in range(10):
    print(test_func(i*2))
