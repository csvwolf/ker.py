"""
monitor module
"""
from datetime import datetime
from ker.utils import request
from .list import API_LIST


class Monitor:
    """
    monitor api
    """
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def get_cpu(self, uuid, start_time, unit, end_time=datetime.utcnow()):
        """
        get monitor info for cpu
        """
        return request(API_LIST.MONITOR_CPU.value, {
            'email': self.email,
            'token': self.token,
            'uuid': uuid,
            'startTime': start_time,
            'endTime': end_time,
            'unit': unit
        })

    def get_net(self, uuid, start_time, unit, end_time=datetime.utcnow()):
        """
        get monitor info for network
        """
        return request(API_LIST.MONITOR_NET.value, {
            'email': self.email,
            'token': self.token,
            'uuid': uuid,
            'startTime': start_time,
            'endTime': end_time,
            'unit': unit
        })

    def get_nat(self, uuid, start_time, unit, end_time=datetime.utcnow()):
        """
        get monitor info for nat
        """
        return request(API_LIST.MONITOR_NAT.value, {
            'email': self.email,
            'token': self.token,
            'uuid': uuid,
            'startTime': start_time,
            'endTime': end_time,
            'unit': unit
        })

    def get_io(self, uuid, start_time, unit, end_time=datetime.utcnow()):
        """
        get monitor info for io
        """
        return request(API_LIST.MONITOR_IO.value, {
            'email': self.email,
            'token': self.token,
            'uuid': uuid,
            'start_time': start_time,
            'end_time': end_time,
            'unit': unit
        })
