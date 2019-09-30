"""
Main usage class for the module
"""
from ker.api import Server
from ker.api import Account
from ker.api import DNS
from ker.api import Monitor
from ker.api import SSH
from ker.utils import HostkerRequestError


class Ker:
    """
    Includes all apis for hostker.
    """
    def __init__(self, email, token):
        self.email = email
        self.token = token
        self.dns = DNS(email, token)
        self.monitor = Monitor(email, token)
        self.server = Server(email, token)
        self.ssh = SSH(email, token)
        self.account = Account(email, token)

    def test(self):
        """
        You can test with: Ker([email], [token]).test()
        """
        try:
            self.account.get_quota()
        except HostkerRequestError:
            return False
        return True
