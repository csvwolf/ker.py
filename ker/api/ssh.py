from ker.utils import request
from ker.api import API_LIST

class SSH:
  def __init__(self, email, token):
    self.email = email
    self.token = token

  def list(self):
    return request(API_LIST.SSH_LIST.value, {
      'email': self.email,
      'token': self.token
    })

  def create(self, name, key):
    return request(API_LIST.SSH_CREATE.value, {
      'email': self.email,
      'token': self.token,
      'name': name,
      'key': key
    })
  
  def delete(self):
    return request(API_LIST.SSH_DELETE.value, {
      'email': self.email,
      'token': self.token
    })