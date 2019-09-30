"""
request creator for hostker common attributes
"""
import requests


class HostkerRequestError(Exception):
    """
    Custom Request Error
    """

def request(path, params):
    """
    request with content-type application/x-www-form-urlencoded and handle error
    """
    res = requests.post(
        f'https://i.hostker.com/api{path}',
        data=params,
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    res.encoding = 'utf-8'
    result = res.json()
    if result['success'] == 0:
        raise HostkerRequestError(result['errorMessage'])
    return result
