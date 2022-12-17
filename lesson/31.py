from datetime import date, datetime, timedelta
import locale
#date
locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
day = date.today()
print(day)
print(day.day, day.month, day.year, day.weekday(), sep="|")
#datetime
now = datetime.now()
naw = datetime.today()
print(naw, now, sep="||")
print(naw, now, sep="||")
print(naw.hour, naw.minute, naw.second, sep="|")
print(naw.strftime("%A"))
print(f"Дата {naw.strftime('%A %d, %B %Y')} время {naw.strftime('%H:%M')}")
print(naw.strftime("%c"))
print(naw.strftime("%x"))
print(naw.strftime("%X"))
f = now + timedelta(days=2, hours= 3, minutes=4)
print(f.strftime("%c"))