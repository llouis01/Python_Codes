'''
program that takes input (name, birthdate) from user and tells them how old they are, when will they turn a hundred 
and how far after New Year's Day they were born. Written in Python 2.
'''

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

today = date.today() # date.var returns date
print(f'\nToday is', (today.strftime('%B')), (today.strftime('%d')), (today.strftime('%Y'))) # time formats used to return mo, day, yr

print("\nHello! What is your name?")
user_name = input('--> ')
print(f'\nHow old are you, {user_name}?')
user_age = int(input('--> '))

# Python lists start with 0 index so add in a dummy for 0
months = ['Dummy', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print('\nWhat day, month and year were you born?')
user_day = int(input('Day: ')) # use this line to get index from months list
user_month = months.index(input('Month: '))
user_year = int(input('Year: ')) 
date_birth = user_year, user_month, user_day



print(f'\nYou were born on {months[user_month]} {user_day}th {user_year}.')

if today.month > user_month or (today.month == user_month and today.day >= user_day):
    NYE_birth = (today.year - user_age, 1, 1)
else:
    NYE_birth = (today.year - user_age - 1, 1, 1) # use this conditional because past january, the program counts everything as a year.

print(f'The New Year\'s Eve of that year was January 1st {user_year}')
print(f'You were born {user_month - 1} month(s) and, {user_day - 1} days after NYE.')


if (user_month == (today.strftime('%B')) and user_day == (today.strftime('%d'))):
    print(f'Happy Birthday, {user_name}!')
else:
    print('\n') # Why is this not working?

# need to include months

if user_month < today.month or (today.month == user_month and today.day <= user_day):
    ry = 100 - user_age
else:
    ry = 100 - user_age - 1
age_cent = date (int(today.year + ry), int(user_month), int(user_day))
print(f'Wow, a long way to go! You will turn 100 years-old on  {age_cent}')
print('\n')
