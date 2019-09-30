"""
ssh module
"""
from ker.utils import request
from .list import API_LIST


class SSH:
    """
    ssh api
    """
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def list(self):
        """
        list ssh keys
        """
        return request(API_LIST.SSH_LIST.value, {
            'email': self.email,
            'token': self.token
        })

    def create(self, name, key):
        """
        create ssh key
        """
        return request(API_LIST.SSH_CREATE.value, {
            'email': self.email,
            'token': self.token,
            'name': name,
            'key': key
        })

    def delete(self):
        """
        delete ssh key
        """
        return request(API_LIST.SSH_DELETE.value, {
            'email': self.email,
            'token': self.token
        })
