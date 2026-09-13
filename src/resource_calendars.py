from datetime import date,timedelta
def is_working_day(d, unavailable=()):
    return d.weekday()<5 and d not in set(unavailable)
def add_workdays(start,days,unavailable=()):
    d=start; left=days
    while left>0:
        d+=timedelta(days=1)
        if is_working_day(d,unavailable):left-=1
    return d
