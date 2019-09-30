from ker.utils import request
from ker.api import API_LIST

class Account:
  def __init__(self, email, token):
    self.email = email
    self.token = token

  def get_quota(self):
    return request(API_LIST.ACCOUNT_QUOTA.value, {'email': self.email, 'token': self.token})
  
  def get_balance(self):
    return request(API_LIST.ACCOUNT_BALANCE.value, {'email': self.email, 'token': self.token})