"""
format time in this format:
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific
notation$
Oct 21 2022$
"""

from datetime import datetime
import calendar as cal

dt = datetime.now()
epoch = datetime(1970, 1, 1)
delta = dt - epoch
print("Seconds since January 1, 1970: " + format(delta.total_seconds(), ',.4f')
      + " or {:.2e}".format(delta.total_seconds()) + " in scientific notation")
time = datetime.now()
month_str = cal.month_name[1]
print(month_str[:3] + time.strftime(" %d %Y"))
