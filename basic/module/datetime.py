# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

now = datetime.now()
print(now)

print(datetime(2019, 7, 12, 22, 46, 34).timestamp())

print(datetime.fromtimestamp(1562899594.0))

print(datetime.utcfromtimestamp(1562899594.0))

print(datetime.strptime('2019-7-12 10:46:00', '%Y-%m-%d %H:%M:%S'))

print(datetime.now().strftime('%a %b %d %H:%M'))

print(datetime.now()+timedelta(days=1))

tz_utc_8 = timezone(timedelta(hours = 10))
print(datetime.now().replace(tzinfo=tz_utc_8))

utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_time = utc_time.astimezone(timezone(timedelta(hours = 8)))
dj_time = utc_time.astimezone(timezone(timedelta(hours = 9)))
print(bj_time.astimezone(timezone(timedelta(hours = 9))))
print(bj_time)