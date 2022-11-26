import requests
obis_base_url = 'https://api.obis.org'

def get(url, args, **kwargs):
    """
    Handles technical details of sending GET request to the API
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
        "Accept-Encoding": "gzip, deflate, br",
        "Host": "api.obis.org",
        "Connection": "keep-alive",
    }
    out = requests.get(url, params=args, headers=headers, **kwargs)
    out.raise_for_status()
    return out.json()