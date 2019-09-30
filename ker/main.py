from ker.api import Server
from ker.api import Account
from ker.api import DNS
from ker.api import Monitor
from ker.api import SSH
from ker.utils import HostkerRequestError

class Ker:
  def __init__(self, email, token):
    self.email = email
    self.token = token
    self.dns = DNS(email, token)
    self.monitor = Monitor(email, token)
    self.server = Server(email, token)
    self.ssh = SSH(email, token)
    self.account = Account(email, token)

  def test(self):
    try:
      self.account.get_quota()
    except HostkerRequestError:
      return False
    return True