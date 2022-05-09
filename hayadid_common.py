import sys

def url_expand(orig_url):
    import urlexpander

    expanded_url = urlexpander.expand(orig_url)
    if expanded_url[-23:]=='_CONNECTIONPOOL_ERROR__':
        print(f"was _CONNECTIONPOOL_ERROR_ expanded_url={expanded_url}", file=sys.stderr)
        expanded_url = expanded_url[0:-25]
    print(f"expanded_url={expanded_url} type={type(expanded_url)}", file=sys.stderr)
    return expanded_url



def tests():
    import profanity_check
    profanity_check.predict(["fuck you",
                             "this is good",
                             "go to hell",
                             "you are not an idiot"
                             "מפגר"])
