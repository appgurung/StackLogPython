from os import path

with open("%s/VERSION" % path.abspath(path.dirname(__file__))) as f:
     version = f.read().strip('\n')

defaults = {
    'DEFAULT_REQUEST_TIMEOUT': 30,
    'MAX_LINE_LENGTH': 32000,
    'FLUSH_INTERVAL_SECS': 5,
    'FLUSH_BYTE_LIMIT': 2 * 1024 * 1024,
    'STACKLOG_URL': 'http://192.168.43.244:8873/api/v1/sandbox/log/create/',
    'BUF_RETENTION_BYTE_LIMIT': 4 * 1024 * 1024,
    'RETRY_INTERVAL_SECS': 8,
    'USER_AGENT': 'python/%s' % version
}
