import requests

class HostkerRequestError(Exception):
  pass

def request(path, params):
  r = requests.post(f'https://i.hostker.com/api{path}', data=params, headers={'Content-Type': 'application/x-www-form-urlencoded'})
  r.encoding = 'utf-8'
  result = r.json()
  if result['success'] == 0:
    raise HostkerRequestError(result['errorMessage'])
  return result