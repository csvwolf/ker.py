"""
dns module
"""
from ker.utils import request
from .list import API_LIST


class DNS:
    """
    dns apis
    """
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def list(self, domain):
        """
        list dns config by domain name
        """
        return request(
            API_LIST.DNS_LIST.value,
            {
                'email': self.email,
                'token': self.token,
                'domain': domain
            }
        )

    def add(self, domain, header, record_type, data, ttl=300, priority=5):
        """
        add dns config by domain name
        """
        return request(
            API_LIST.DNS_ADD.value,
            {
                'email': self.email,
                'token': self.token,
                'domain': domain,
                'header': header,
                'type': record_type,
                'data': data,
                'ttl': ttl,
                'priority': priority
            }
        )

    def edit(self, unique_id, data, ttl=300, priority=5):
        """
        edit dns config by id
        """
        return request(
            API_LIST.DNS_EDIT.value,
            {
                'email': self.email,
                'token': self.token,
                'id': unique_id,
                'data': data,
                'ttl': ttl,
                'priority': priority
            }
        )

    def delete(self, unique_id):
        """
        delete dns config by id
        """
        return request(
            API_LIST.DNS_DELETE.value,
            {
                'email': self.email,
                'token': self.token,
                'id': unique_id
            }
        )
