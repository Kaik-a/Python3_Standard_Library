# Calendar Module
from datetime import datetime, timedelta
import calendar

now = datetime.now()

test_date = now + timedelta(days=2)
my_first_linkedin_cours = now - timedelta(weeks=3)
print(test_date.date())

if test_date > my_first_linkedin_cours:
    print('Comparaison works')

cal = calendar.month(2001, 10)
print(cal)

cal2 = calendar.month(2001, 10, 11)
print(cal2)

print(calendar.isleap(1999))
print(calendar.isleap(2000))
