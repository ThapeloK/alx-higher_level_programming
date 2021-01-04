#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    results = None
    try:
        results = fct(*args)
        return results
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return results
