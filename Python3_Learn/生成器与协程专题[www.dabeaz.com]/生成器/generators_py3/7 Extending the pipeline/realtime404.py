# realtime404.py
# 实时打印404请求日志
# Print all 404 requests as they happen in the log

from apachelog import *
from follow import *

logfile = open("access-log")
loglines = follow(logfile)
log = apache_log(loglines)

r404 = (r for r in log if r['status'] == 404)

for r in r404:
    print(r['host'], r['datetime'], r['request'])
