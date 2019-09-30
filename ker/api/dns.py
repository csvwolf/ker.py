from ker.utils import request
from ker.api import API_LIST

class DNS:
  def __init__(self, email, token):
    self.email = email
    self.token = token

  def list(self, domain):
    return request(
      API_LIST.DNS_LIST.value,
      {
        'email': self.email,
        'token': self.token,
        'domain': domain
      }
    )
  
  def add(self, domain, header, type, data, ttl = 300, priority = 5):
    return request(
      API_LIST.DNS_ADD.value,
      {
        'email': self.email,
        'token': self.token,
        'domain': domain,
        'header': header,
        'type': type,
        'data': data,
        'ttl': ttl,
        'priority': priority
      }
    )

  def edit(self, id, data, ttl = 300, priority = 5):
    return request(
      API_LIST.DNS_EDIT.value,
      {
        'email': self.email,
        'token': self.token,
        'id': id,
        'data': data,
        'ttl': ttl,
        'priority': priority
      }
    )
  
  def delete(self, id):
    return request(
      API_LIST.DNS_DELETE.value,
      {
        'email': self.email,
        'token': self.token,
        'id': id
      }
    )