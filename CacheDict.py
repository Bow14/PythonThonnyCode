from __future__ import print_function, division

cache_dict = {}

def cache_function(e, c):
  
    if e == 0:
        return c+1
    elif c == 0:
        return cache_function(e-1, 1)

    if (e, c) in cache_dict:
        return cache_dict[e, c]
    else:
        cache_dict[e, c] = cache_function(e-1, cache_function(e, c-1))
        return cache_dict[e, c]


print(cache_function(2, 8))
print(cache_function(2, 9))