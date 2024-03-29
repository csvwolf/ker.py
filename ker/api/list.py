"""
api list module
"""
from enum import Enum


class API_LIST(Enum):
    """
    api uri list
    """
    ACCOUNT_QUOTA = '/quota'
    ACCOUNT_BALANCE = '/balance'
    SSH_LIST = '/listSshKey'
    SSH_CREATE = '/createSshKey'
    SSH_DELETE = '/deleteSshKey'
    SERVERS_LIST = '/listServers'
    SERVER_GET = '/getServer'
    SERVER_CREATE = '/createServer'
    SERVER_SET_POWER = '/setPower'
    SERVER_SET = '/setServer'
    SERVER_REINSTALL = '/reinstallServer'
    SERVER_DELETE = '/deleteServer'
    MONITOR_CPU = '/cpuMonitor'
    MONITOR_NET = '/netMonitor'
    MONITOR_NAT = '/natMonitor'
    MONITOR_IO = '/IOMonitor'
    DNS_LIST = '/dnsGetRecords'
    DNS_ADD = '/dnsAddRecord'
    DNS_EDIT = '/dnsEditRecord'
    DNS_DELETE = '/dnsDeleteRecord'
