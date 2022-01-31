import requests
import cbor
import time
import urllib3

from utils.response import Response

def download(url, config, logger=None):
    port = 443
    while True:
        try:
            print("get: " + url)
            resp = requests.get(url)
            break
        except urllib3.exceptions.MaxRetryError:

            resp = requests.get("https://google.com")
            resp.status_code = 404
            break
        except:
            resp = requests.get("https://google.com")
            resp.status_code = 404
            break
    if resp.status_code is None:
        logger.error(f"Spacetime Response error {resp} with url {url}.")
        return Response({
            "error": f"Spacetime Response error {resp} with url {url}.",
            "status": resp.status_code,
            "url": url})
    return resp
