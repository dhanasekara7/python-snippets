```python

# date

# time
 
# datetime
import datetime
datetime.date(year = 2020, month = 5, day = 3)

d = datetime.date.today()
d.year
d.month
d.day

datetime.date.fromtimestamp(24*60*60)
#datetime.date(1970, 1, 2)

datetime.date.fromordinal(1)
#datetime.date(1, 1, 1)

>>> datetime.date.today().weekday()
# 6
# monday = 0, sunday = 6
>>> datetime.date.today().isoweekday()
7
# monday = 1, sunday = 7

d = datetime.date.today()
d
#datetime.date(2020, 5, 3)
d.isoformat()
#'2020-05-03'

d.strftime('%A %d %B %Y')
#'Sunday 03 May 2020'

"the date is {:%A %d %B %Y}".format(d)
#'the date is Sunday 03 May 2020'

# portable way
"{date:%A} {date.day} {date:%B} {date.year}".format(date=d)
#'Sunday 3 May 2020'

>>> datetime.date.min
datetime.date(1, 1, 1)
>>>
>>> datetime.date.max
datetime.date(9999, 12, 31)
>>>
>>> datetime.date.resolution
datetime.timedelta(days=1)


# timedelta

# arithmetic with datetime

# timezone --> tzinfo

```