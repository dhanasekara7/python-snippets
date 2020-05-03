```python

datetime.time(3, 1, 2, 232)
#datetime.time(3, 1, 2, 232)

datetime.time(hour=23, minute=59, second=59, microsecond=999999)
#datetime.time(23, 59, 59, 999999)

t = datetime.time(10, 32, 47, 323902)

t.hour

t.minute

t.second

t.microsecond

t.isoformat()
#'10:32:47.323902'

# represented using non-portable version
t.strftime("%Hh%Mm%Ss")
#'10h32m47s'

#pythonic way
"{t.hour}h{t.minute}m{t.second}s".format(t=t)
#'10h32m47s'

>>> datetime.time.min
datetime.time(0, 0)
>>>
>>> datetime.time.max
datetime.time(23, 59, 59, 999999)
>>> datetime.time.resolution
datetime.timedelta(microseconds=1)

# datetimes combined
from datetime import datetime as Datetime
import datetime as dt

>>> datetime.datetime.today()
datetime.datetime(2020, 5, 3, 17, 51, 53, 997728)
>>>
### timezone specific
>>> datetime.datetime.now()
datetime.datetime(2020, 5, 3, 17, 52, 0, 119198)

datetime.datetime.utcnow()
datetime.datetime(2020, 5, 3, 8, 53, 5, 417586)

>>> datetime.datetime.fromordinal(5)
datetime.datetime(1, 1, 5, 0, 0)
>>>
>>> datetime.datetime.fromtimestamp(3635352)
datetime.datetime(1970, 2, 12, 10, 49, 12)

>>> datetime.datetime.utcfromtimestamp(3635352)
datetime.datetime(1970, 2, 12, 1, 49, 12)

# today 8:15
>>> d = datetime.datetime.today()
>>> t = datetime.time(8, 15)
>>>
>>> datetime.datetime.combine(d, t)
datetime.datetime(2020, 5, 3, 8, 15)

>>> dt = datetime.datetime.strptime("Monday 6 January 2014, 12:13:31", "%A %d %B %Y, %H:%M:%S")
>>> dt
datetime.datetime(2014, 1, 6, 12, 13, 31)

>>> dt.date()
datetime.date(2014, 1, 6)
>>>
>>> dt.time()
datetime.time(12, 13, 31)

>>> dt.day
6
>>>
>>> dt.isoformat()
'2014-01-06T12:13:31'

### Duration
>>> datetime.timedelta(milliseconds=1, microseconds=1000)
datetime.timedelta(microseconds=2000)
>>>

>>> td = datetime.timedelta(weeks = 1, minutes = 2, milliseconds = 5500)
>>> td
datetime.timedelta(days=7, seconds=125, microseconds=500000)
>>> td.days
7
>>> td.seconds
125
>>>
>>> td.microseconds
500000

>>> str(td)
'7 days, 0:02:05.500000'
>>>
>>> repr(td)
'datetime.timedelta(days=7, seconds=125, microseconds=500000)'
>>>
>>> td
datetime.timedelta(days=7, seconds=125, microseconds=500000)

# date time arithmetic
>>> a = datetime.datetime(year=2014, month=5, day=8)
>>> b = datetime.datetime(year=2014, month=3, day=14)
>>>
>>> d = a - b
>>> d
datetime.timedelta(days=55)
>>> d.days
55

>>> datetime.date.today()
datetime.date(2020, 5, 3)
>>>
>>> datetime.date.today() + datetime.timedelta(weeks=1)*3
datetime.date(2020, 5, 24)
>>>

# arithmetic on simple "time" object is not supported
>>> f = datetime.time(14, 30, 0)
>>> g = datetime.time(15, 45, 0)
>>>
>>> f - g
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.time'
>>>
>>>

# timezones

>>> cet = datetime.timezone(datetime.timedelta(hours=1), "CET")
>>> cet
datetime.timezone(datetime.timedelta(seconds=3600), 'CET')
>>>
>>> departure = datetime.datetime(year=2014, month=1, day=7, hour=11, minute=30,tzinfo=cet)
>>>
>>> arrival = datetime.datetime(year=2014, month=1, day=7, hour=13, minute=5,tzinfo=datetime.timezone.utc)
>>>
>>> arrival - departure
datetime.timedelta(seconds=9300)
>>>
>>> str(arrival - departure)
'2:35:00'

```