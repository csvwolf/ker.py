"""
server module
"""
from ker.utils import request
from .list import API_LIST


class Server:
    """
    server apis
    """
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def list(self):
        """
        list all servers
        """
        return request(API_LIST.SERVERS_LIST.value, {
            'email': self.email,
            'token': self.token
        })

    def get(self, uuid):
        """
        get one server by uuid
        """
        return request(API_LIST.SERVER_GET.value, {
            'email': self.email,
            'token': self.token,
            'uuid': uuid
        })


    def create(self, name, memory, area, os, ssh_key):
        """
        create a server
        """
        return request(API_LIST.SERVER_CREATE.value, {
            'email': self.email,
            'token': self.token,
            'name': name,
            'memory': memory,
            'area': area,
            'os': os,
            'sshKey': ssh_key
        })


    def set_power(self, uuid, power):
        """
        set power for server by uuid
        """
        return request(API_LIST.SERVER_SET_POWER.value, {
            'email': self.email,
            'token': self.token,
            'uuid': uuid,
            'power': power
        })


    def set(self, uuid, close_disk_virt_io, close_net_virt_io, iso, boot_order):
        """
        set server by uuid
        """
        return request(API_LIST.SERVER_SET.value, {
            'email': self.email,
            'token': self.token,
            'uuid': uuid,
            'closeDiskVirtIO': close_disk_virt_io,
            'closeNetVirtIO': close_net_virt_io,
            'iso': iso,
            'bootOrder': boot_order
        })

    def reinstall(self, uuid, os, ssh_key):
        """
        reinstall a server
        """
        return request(API_LIST.SERVER_REINSTALL.value, {
            'email': self.email,
            'token': self.token,
            'uuid': uuid,
            'os': os,
            'sshKey': ssh_key
        })

    def delete(self, uuid):
        """
        delete a server by uuid(no confirm or recycle bin!!)
        """
        return request(API_LIST.SERVER_DELETE.value, {
            'email': self.email,
            'token': self.token,
            'uuid': uuid
        })
