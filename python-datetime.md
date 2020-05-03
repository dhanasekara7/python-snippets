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



# timedelta

# arithmetic with datetime

# timezone --> tzinfo

```