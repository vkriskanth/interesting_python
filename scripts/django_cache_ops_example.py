#Function caching
from cacheops import cached_as

"""
 Django-cacheops is a Django application that uses Redis to provide advanced caching capabilities, 
 including automatic query caching and event-based automatic caching.
  It can speed up Django applications by reducing data load and has features like function and view caching.
  This is not a working example.
"""

@cached_as(Article, timeout = 120)

def article_stats():
    return {
        'tags': list(Article)
    }
