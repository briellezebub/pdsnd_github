import time
import pandas as pd
import numpy as np

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or " all " to apply no month filter
        (str) day - name of the day of the week to filter by, or " all " to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter city name (Chicago, New York City, or Washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid city name. Please choose from Chicago, New York City, or Washington.')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter month (all, january, february, ... , june): ').lower()
        if month in MONTHS or month == 'all':
            break
        else:
            print('Invalid month. Please choose a valid month or " all ".')
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day of the week (all, monday, tuesday, ... sunday): ').lower()
        if day in DAYS or day == 'all':
            break
        else:
            print('Invalid day of the week. Please choose a valid day or " all ".')
    
    print('-' * 40)
    return city, month, day
