from datetime import datetime
from ker.utils import request
from ker.api import API_LIST

class Monitor:
  def __init__(self, email, token):
    self.email = email
    self.token = token

  def get_cpu(self, uuid, start_time, unit, end_time = datetime.utcnow()):
    return request(API_LIST.MONITOR_CPU.value, {
      'email': self.email,
      'token': self.token,
      'uuid': uuid,
      'startTime': start_time,
      'endTime': end_time,
      'unit': unit
    })

  def get_net(self, uuid, start_time, unit, end_time = datetime.utcnow()):
    return request(API_LIST.MONITOR_NET.value, {
      'email': self.email,
      'token': self.token,
      'uuid': uuid,
      'startTime': start_time,
      'endTime': end_time,
      'unit': unit
    })
  
  def get_nat(self, uuid, start_time, unit, end_time = datetime.utcnow()):
    return request(API_LIST.MONITOR_NAT.value, {
      'email': self.email,
      'token': self.token,
      'uuid': uuid,
      'startTime': start_time,
      'endTime': end_time,
      'unit': unit
    })

  def get_io(self, uuid, start_time, unit, end_time = datetime.utcnow()):
    return request(API_LIST.MONITOR_IO.value, {
      'email': self.email,
      'token': self.token,
      'uuid': uuid,
      'start_time': start_time,
      'end_time': end_time,
      'unit': unit
    })