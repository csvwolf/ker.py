"""
account module
"""
from ker.utils import request
from .list import API_LIST


class Account:
    """
    all account apis
    """
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def get_quota(self):
        """
        get quota infomation for user
        """
        return request(API_LIST.ACCOUNT_QUOTA.value, {'email': self.email, 'token': self.token})

    def get_balance(self):
        """
        get balance information for user
        """
        return request(API_LIST.ACCOUNT_BALANCE.value, {'email': self.email, 'token': self.token})
