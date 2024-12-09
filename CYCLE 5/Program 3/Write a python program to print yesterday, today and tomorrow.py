import datetime as m
today=m.date.today()
yesterday=today-m.timedelta(days=1)
tommorrow=today+m.timedelta(days=1)
print("yesterday:",yesterday,"   Today:",today,"   tommorrow:",tommorrow)
